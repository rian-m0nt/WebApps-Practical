from django.urls import path
from . import views

app_name='stories'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:story_id>/', views.article, name='article'),


]
