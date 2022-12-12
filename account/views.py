from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import views as auth_view , authenticate , login
from Home import views as home_view
from .forms import Recruit
from .models import CustomUser
from User.models import Member
from django.http import HttpResponse
from django.contrib.auth import get_user_model


User = get_user_model()

def homepage(request):
    return render(request, "member_dashboard.html")


def recruit(request):
    form = Recruit()
    return render(request, "recruit.html")

def recruit_save(request):
    if request.method == "POST":
        user = CustomUser()
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.user_type = request.POST.get('role')

        user.save()
     
        # session is logged in
        context = {'username' : user.username}
        user = CustomUser.objects.filter(email=user.email).values().first()

        # request.session['member_id'] = user['username']
        # return render(request, "test.html", {'id':context})
        return render(request, "member_dashboard.html", context)
    else:
        return HttpResponse('<h1>Form was invalid</h1>') 


def all_members(request):
    userlist = CustomUser.objects.all()
    return render(request, "userlist.html",{
        "userlist":userlist
    })


def login_1(request):
    if request.method=='POST':
        # print(request.POST)
        email_id = request.POST.get('email')
        password1 = request.POST.get('password')
        # return render(request, "test.html", {'email_id': email_id, 'password1': password1})
        # user1 = authenticate(request, email=email_id, password=password1)
        user = CustomUser.objects.filter(email=email_id, password=password1).values().first()
        
        # return render(request, "test.html", {'user': user})        
        if user==None:
            return redirect('login') #show that information is incorrect-->redirect to login
        else:
            # return HttpResponse('<h1>Form was invalid</h1>') #just to check
            request.session['member_id'] = user['id']
            # to get: selected_project_id = request.session.get('selected_project_id')

            # return render(request, "test.html", {'id': request.session['member_id']})        
            if user["user_type"] == 'Member':
                return render(request, "member_dashboard.html")
            elif user["user_type"] == 'Director':
                return render(request, "member_dashboard.html")
            elif user["user_type"] == 'Executive Council':
                return render(request, "member_dashboard.html")
            elif user["user_type"] == 'Assistant Director':
                return render(request, "member_dashboard.html")
            elif user["user_type"] == 'Sponsor':
                return render(request, "member_dashboard.html")
            elif user["user_type"] == 'Patron':
                return render(request, "member_dashboard.html")
           


def login_view(request):
    return render(request,'login.html')


def logout(request):
    return render(request,'login.html')


def view(request):
    user_first_name = request.user.first_name
    info = CustomUser.objects.all().filter(first_name=user_first_name)
    return render(request, 'profile/show.html', {'info': info})

def contact(request):
    user_email = request.email

def addbudget(request):
    return render(request, "financial_records.html")

def promotions(request):
    return render(request, "promotions.html")