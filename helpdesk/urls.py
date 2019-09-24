from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('add_incident', views.add_incident, name='add_incident'),
    path('open/<int:inc_id>', views.open_incident, name='open_incident'),
    path('changestate/<int:inc_id>/<str:state>', views.changestate, name='changestate'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)