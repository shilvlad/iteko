from .models import Profile, ProfileBasicSettings

from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        labels = {

        }


class ProfileBasicSettingsForm(ModelForm):
    class Meta:
        model = ProfileBasicSettings
        fields = '__all__'
        labels = {
        }

