
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_view,name='register'),

    path('index/',views.index_view,name='index'),
    path('login/',views.login_view,name='login'),
    path('form/',views.form_view,name='form'),
    path('usercreationform/',views.usercreation_view,name='usercreationform'),

]
