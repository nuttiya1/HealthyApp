from django.db import models

class Activity(models.Model):
   activity_text = models.CharField(max_length=200)

#class List(models.Model):
#    pass

#class Data(models.Model):
#    text = models.TextField(default='')
    #list = models.ForeignKey(List, default=None)

# Anyone has there own information such as name weight
# activity

#class Person(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#    activity_text = models.CharField(max_length=20)
