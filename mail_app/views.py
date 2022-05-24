from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.



def mail_view(request):
    subject='greetings'
    msg='congratulations for your success'
    to='mehtariti82@gmail.com'
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if (res==1):
        msg='sent mail successfully'

    else:
        msg='mail could not sent'

    return HttpResponse(msg)