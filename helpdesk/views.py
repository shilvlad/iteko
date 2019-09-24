from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
from django.views.generic import CreateView

from .forms import IncidentForm

from .models import HelpDeskRoles, HelpDeskUsers, HelpDeskIncidents



@login_required
def index(request):
    template = loader.get_template('helpdesk/index.html')
    helpdeskuser = HelpDeskUsers.objects.get(user = request.user)
    helpdeskuserroles = list(helpdeskuser.role.all().values_list('role', flat=True))

    form = IncidentForm()
    form.fields['user'].queryset = HelpDeskUsers.objects.filter(user = request.user)
    form.fields['user'].empty_label = None
    #form.fields['user'].selected = 2

    #own_incidents = HelpDeskIncidents.objects.filter(user = request.user)
    own_incidents = HelpDeskIncidents.objects.all()

    print(form)
    context = {
        'helpdeskuser' : helpdeskuser,
        'helpdeskuserroles' : helpdeskuserroles,
        'form' : form,
        'own_incidents': own_incidents,
    }


    return HttpResponse(template.render(context, request))


@login_required
def add_incident(request):
    if request.method == 'POST':
        print(request.POST)
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Пиздец какой-то")

        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

