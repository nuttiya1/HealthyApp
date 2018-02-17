from django.db import models

class Activity(models.Model):
    activity_text = models.CharField(max_length=200)
