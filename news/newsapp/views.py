from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Story
from django.template import loader
# Create your views here.

def index(request):
    latest_story_list = Story.objects.order_by('-publication_date')[:5]

    context = {
        'latest_story_list': latest_story_list,
    }
    return render(request, 'newsapp/index.html', context)

def article(request, story_id):
    try:
        story = Story.objects.get(pk=story_id)
    except Story.DoesNotExist:
        raise Http404("Story does not exist")
    return HttpResponse("You're looking at story %s" % story_id)
