from django.urls import path
from specific.views import *
app_name='specific'
urlpatterns=[
    path('ravi/',ravi,name='ravi'),
    path('mukul/',ravi,name='mukul'),
]