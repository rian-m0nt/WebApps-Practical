from django.shortcuts import render, get_object_or_404
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

    article = get_object_or_404(Story,pk=story_id)

    return render(request, 'newsapp/article.html', {'article': article})
