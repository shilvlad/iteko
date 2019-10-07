from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.conf.urls.static import static
from .models import MainNews


def index(request):
    template = loader.get_template('main/index.html')
    news = MainNews.objects.all()

    context = {
        'news': news,
    }
    print (news)
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('main/about.html')
    context = {
        #'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

