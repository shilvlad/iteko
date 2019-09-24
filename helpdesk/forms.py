from django.forms import ModelForm
from .models import HelpDeskIncidents




class IncidentForm(ModelForm):
    class Meta:
        model = HelpDeskIncidents
        fields = '__all__'
        #fields = ['user', 'incident_type', 'description', ]
        exclude = ['timestamp_created']
        labels = {
            "description": "Описание",
        }