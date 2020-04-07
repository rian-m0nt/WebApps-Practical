from django.db import models

# Create your models here.
class Story(models.Model):
    story_title = models.CharField(max_length=255)
    publication_date = models.DateTimeField('Published On')
    story_text = models.CharField(max_length=500)
