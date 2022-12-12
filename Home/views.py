from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "login.html")

def home_members(request):
    return render(request, "member_dashboard.html")
