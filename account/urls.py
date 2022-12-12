from django.urls import path
from . import views
# from django.contrib.auth import views as auth_view
urlpatterns = [
    path('recruit/', views.recruit, name='recruit'),
    path('recruit_save', views.recruit_save, name='recruit-save'),
    path('', views.login_view , name='login-page'),
    path('login', views.login_1 , name='login'),
    path('logout', views.logout,name='logout'),
    path('members', views.all_members),
    path('memberhome', views.homepage),
    path('add_budget', views.addbudget),
    path('promotions', views.promotions),

]
