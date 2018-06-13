from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^test/(?P<search>\w{1,50})/$', views.genderSearch),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #resimleri belirtilen yola yukler
