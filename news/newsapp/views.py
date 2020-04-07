from django.shortcuts import render
from django.http import HttpResponse
from .models import Story
from django.template import loader
# Create your views here.

def index(request):
    latest_story_list = Story.objects.order_by('-publication_date')[:5]
    template = loader.get_template('newsapp/index.html')
    context = {
        'latest_story_list': latest_story_list,
    }
    return HttpResponse(template.render(context, request))

def article(request, story_id):
    return HttpResponse("You're looking at story " % story_id)
