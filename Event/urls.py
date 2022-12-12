from django.urls import path
from . import views
# from demoapp import views

urlpatterns = [
    # path('<int:year>/<str:month>/', views.events),
    path('events/', views.all_events),
    path('add_event', views.add_event),
    path('save_event', views.save_event)
]