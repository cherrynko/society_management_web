from django.urls import path
from . import views
from User import views as user_views
urlpatterns = [
    path('',views.home, name='Home'),
    path('members/', views.home_members, name='Members'),
    # path('recruit/', user_views.register, name='recruit'),
]
