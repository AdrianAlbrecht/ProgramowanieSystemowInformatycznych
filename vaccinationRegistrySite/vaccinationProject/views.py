from django.shortcuts import render
from django.http import HttpResponse, request
import datetime

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from .serializers import FacilitySerializer
from django.core.signing import Signer
from django.core.mail import send_mail, EmailMessage

import logging

def index(request):
    context={
        'name':'janek',
        'phone_number':666555444
    }
    return render(request, 'result.html',context)
    # return HttpResponse("Hello, world. You're at the vaccination page.")

def createUser(request):
    user=User.objects.create_user('kakakkak','luft@dzbanek.pl','zaq1@WSX')
    context={
        'result':'Username %s Email %s' % (user.username, user.email)
    }
    return render(request, 'result.html',context)

def changePassword(request):
    user=User.objects.get(username='janek')
    user.set_password('!@#asdasdas')
    user.save()
    context={
        'result':'Username %s Password %s' % (user.get_full_name(), user.password)
    }
    return render(request,'result.html',context)

def setValue(request):
    cache.set('hello_key','Hello World!',100)
    context={
        'result':cache.get('hello_key')
    }
    return HttpResponse(context)

def signing(request):
    signer=Signer()
    value=signer.sign('Mystring')
    original = signer.unsign(value)
    context={
        'result':'Value %s Original %s' % (value,original)
    }
    return render(request, 'result.html', context)
def saltArgument(request):
    singer=Signer()
    value= singer.sign('Mystring')
    signer=Signer(salt='extra')
    saltValue=signer.sign('Mystring')
    context={
        'result':'Value %s Salt value %s' %(value,saltValue)
    }
    return render(request, 'result.html', context)

def sendMail(request):
    send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,)
    return HttpResponse()

def sendObjectMail(request):
    logger=logging.getLogger('helloworld_info').info('Object mail sent')
    email=EmailMessage(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    reply_to=['reply@gmail.com'],).send()
    return HttpResponse()

