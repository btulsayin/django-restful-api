# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import io

import json

def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image

@csrf_exempt
def genderSearch(request, search=None):
    # if request.method == 'POST':
    #     return HttpResponse(json.dumps({"success": True, "result": "POST"}),
    #                         content_type="application/json")
    # return HttpResponse(json.dumps({"success": False, "result": "GET"}),
    #                     content_type="application/json")

    data = {"success": False}
    if request.method == 'POST':
        if request.FILES["img_binarydata"]:
            try:
                # read the image in PIL format
                image = request.FILES["img_binarydata"].read()
                image = Image.open(io.BytesIO(image))

                # preprocess the image and prepare it for classification
                image = prepare_image(image, target=(224, 224))

                # classify the input image and then initialize the list
                # of predictions to return to the client
                model = ResNet50(weights="imagenet")
                preds = model.predict(image)
                results = imagenet_utils.decode_predictions(preds)
                data["predictions"] = []

                # loop over the results and add them to the list of
                # returned predictions
                for (imagenetID, label, prob) in results[0]:
                    r = {"label": label, "probability": float(prob)}
                    data["predictions"].append(r)
                data["success"] = True
            except:
                pass

    return HttpResponse(json.dumps({"success": True, "result": data}), content_type="application/json")