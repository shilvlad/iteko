from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.conf.urls.static import static


def index(request):


    template = loader.get_template('main/index.html')
    context = {
        #'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('main/about.html')
    context = {
        #'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

