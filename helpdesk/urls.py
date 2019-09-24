from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('add_incident', views.add_incident, name='add_incident')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)