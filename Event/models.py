from django.db import models
import datetime


# Create your models here.
class Event(models.Model):
    event_id = models.IntegerField()
    event_name = models.CharField(max_length=120)
    event_head = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    event_venue = models.CharField(max_length=120)
    dept_id = models.IntegerField()
    num_team_members = models.IntegerField()
    sponsor_id = models.IntegerField()
    sponsor_name = models.CharField(max_length=120)
    budget = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.event_name

