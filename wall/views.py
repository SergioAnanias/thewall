from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse
import bcrypt
from .decorators import loginauth
# Create your views here.

@loginauth
def wall(request):
    context = {
        "usuario": User.objects.get(id=request.session['user']),
        "posts": Message.objects.all(),
        "comments": Comment.objects.all(),
    }
    return render(request, 'wall.html', context)

def newmessage(request):
    print(request.POST)
    newmessage= Message.objects.create(
        message=request.POST['post'],
        user=User.objects.get(id=request.session['user'])
    )
    return JsonResponse({'msg':newmessage.message}, status=200)

def newcomment(request):
    print(request.POST)
    newcomment=Comment.objects.create(
        comment=request.POST['cont'],
        message= Message.objects.get(id=request.POST['post']),
        user = User.objects.get(id=request.session['user'])
    )
    return JsonResponse({'comment':newcomment.comment}, status=200)