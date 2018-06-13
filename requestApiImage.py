import requests
import os

# USAGE:  python simple_request.py
KERAS_REST_API_URL = "http://localhost:8000/test/search/?"

imagePath = os.path.join(os.getcwd(), "images")

for image_name in os.listdir(imagePath):
	IMAGE_PATH = os.path.join(imagePath, image_name) # image path

	# load the input image and construct the payload for the request
	image = open(IMAGE_PATH, "rb").read()
	# print(image)
	payload = {"img_binarydata": image}

	# submit the request
	r_person = requests.post(KERAS_REST_API_URL, files=payload)
	response_data = r_person.json()
	person = {"person": response_data["result"]}

	print(person)
