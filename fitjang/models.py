from django.db import models
from django.utils import timezone

class Activity(models.Model):
    activity_text = models.TextField(default='')
    weight_data = models.PositiveIntegerField(default=0)
    amount_of_time = models.PositiveIntegerField(default=0)
    mets = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.activity_text

# class Weight(models.Model):
#     weight_data = models.PositiveIntegerField(default=0)
#
# class Time(models.Model):
#     amount_of_time = models.PositiveIntegerField(default=0)
#
# class Date(models.Model):
#     date = models.DateTimeField(auto_now=True)


#class Data(models.Model):
#    text = models.TextField(default='')
    #list = models.ForeignKey(List, default=None)

# Anyone has there own information such as name weight
# activity

#class Person(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#    activity_text = models.CharField(max_length=20)
