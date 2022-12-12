from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ("event_id", "event_name", "event_head", "event_date", "event_venue", "dept_id", "num_team_members", "sponsor_id", "sponsor_name", "budget", "description")

        labels = { "event_id":"",
        "event_name":"",
        "event_date":"",
        "event_venue":"",
        "dept_id":"",
        "num_team_members":"",
        "sponsor_id":"",
        "sponsor_name":"",
        "budget":"",
        }

        widgets = { "event_id":forms.NumberInput(attrs={"class":"form-control"}),
        "event_name":forms.TextInput(attrs={"class":"form-control"}),
        "event_date":forms.DateTimeInput(attrs={"class":"form-control"}),
        "event_venue":forms.TextInput(attrs={"class":"form-control"}),
        "dept_id":forms.NumberInput(attrs={"class":"form-control"}),
        "num_team_members":forms.NumberInput(attrs={"class":"form-control"}),
        "sponsor_id":forms.NumberInput(attrs={"class":"form-control"}),
        "sponsor_name":forms.TextInput(attrs={"class":"form-control"}),
        "budget":forms.NumberInput(attrs={"class":"form-control"}),
        }

