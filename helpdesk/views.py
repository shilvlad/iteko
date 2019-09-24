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
from django.utils import timezone

from .forms import IncidentForm

from .models import HelpDeskRoles, HelpDeskUsers, HelpDeskIncidents
import logging

logger = logging.getLogger(__name__)

@login_required
def index(request):

    template = loader.get_template('helpdesk/index.html')
    helpdeskuser = HelpDeskUsers.objects.get(user = request.user)
    helpdeskuserroles = list(helpdeskuser.role.all().values_list('role', flat=True))

    form = IncidentForm()
    form.fields['user'].queryset = HelpDeskUsers.objects.filter(user = request.user)
    form.fields['user'].empty_label = None

    own_incidents = HelpDeskIncidents.objects.filter(user = HelpDeskUsers.objects.get(user = request.user))
    #own_incidents = HelpDeskIncidents.objects.all()

    users_incidents = HelpDeskIncidents.objects.all()
    new_incidents = HelpDeskIncidents.objects.filter(state='new')
    print (request.user.first_name)
    context = {
        'helpdeskuser' : helpdeskuser,
        'helpdeskuserroles' : helpdeskuserroles,
        'form' : form,
        'own_incidents': own_incidents,
        'users_incidents': users_incidents,
        'new_incidents':new_incidents,
    }

    return HttpResponse(template.render(context, request))


@login_required
def add_incident(request):
    if request.method == 'POST':


        form = IncidentForm(request.POST)
        form.user = HelpDeskUsers.objects.filter(user = request.user)

        if form.is_valid():
            form.save()
        else:
            logger.error('Something went wrong!')

        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_accessible_states(inc):
    if inc.state == 'new':
        accessible_buttons = ('worked','wait')
    if inc.state == 'worked':
        accessible_buttons = ('done','wait' )
    if inc.state == 'wait':
        accessible_buttons = ('worked',)
    if inc.state == 'done':
        accessible_buttons = ('closed','rework')
    if inc.state == 'rework':
        accessible_buttons = ('wait','worked')
    if inc.state == 'closed':
        accessible_buttons = ()
    return accessible_buttons

@login_required
def open_incident(request, inc_id):
    template = loader.get_template('helpdesk/open_inc.html')
    inc = HelpDeskIncidents.objects.get(id=inc_id)
    accessible_buttons = get_accessible_states(inc)

    context = {
        'inc' : inc,
        'accessible_buttons' : accessible_buttons,
    }
    return HttpResponse(template.render(context, request))

@login_required
def changestate(request, inc_id, state):
    template = loader.get_template('helpdesk/open_inc.html')
    inc = HelpDeskIncidents.objects.get(id=inc_id)
    if state in get_accessible_states(inc):
        inc.state = state
        inc.save()
    else:
        logger.error('Ошибка смены состояния')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

