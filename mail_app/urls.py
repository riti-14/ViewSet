from django.urls import path
from .views import *
urlpatterns = [
 
    path('mail/',mail_view,name='mail'),
]