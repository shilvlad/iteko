from django.contrib import admin
from .models import HelpDeskRoles, HelpDeskUsers, HelpDeskIncidents


# Register your models here.
admin.site.register(HelpDeskRoles)
admin.site.register(HelpDeskUsers)
admin.site.register(HelpDeskIncidents)