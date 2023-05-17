from django.urls import path
from .views import *


app_name = 'course'

urlpatterns = [
    path('',courses,name='course'),
    path('trainers/',trainers,name='trainers'),
    path('events/',events,name='events'),
    path('pricing/',pricing,name='pricing'),
]
