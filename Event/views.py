from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from .models import Event
from .forms import EventForm
from account.models import CustomUser


# Create your views here.

def events(request, year, month):
    name = "ayesha"
    # convert from month from name to num
    month = month.title()
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)

    # create calender
    cal = HTMLCalendar().formatmonth(year, month_num)


    return render(request, "calender.html", {
        "name": name,
        "year":year,
        "month":month_num,
        "cal":cal,
    })

def all_events(request):
    event_list = Event.objects.all()
    return render(request, "event_list.html",{
        "event_list":event_list
    })
    
def add_event(request):
    # submitted = False
    # if request.method == "POST":
    #     form = EventForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # return render(request,
    # else:
    #     form = EventForm
    #     if 'submitted' in request.GET:
    #         submitted = True
    return render(request, 'add_events.html')


def save_event(request):
    if request.method == 'POST':
        if request.POST.get('event-id') and request.POST.get('dept') and request.POST.get('budget'):
            event = Event()
            event.event_id = request.POST.get('event-id')
            event.event_name = request.POST.get('event-name')
            event.event_date = request.POST.get('date')
            event.dept_id = 1
            event.event_venue = request.POST.get('venue')
            event.num_team_members = request.POST.get('num_members')
            event.sponsor_id= request.POST.get('spon_id')
            event.sponsor_name = request.POST.get('spon_name')
            event.budget = request.POST.get('budget')

            event.save()

            return render(request,'member_dashboard.html')
        
        else:
            return render(request, 'add_events.html')

