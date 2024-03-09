from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import authenticate,login
# from SocialMedia.users.forms import LoginForm   # another way below 
from .forms import LoginForm
# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username =data["username"],password=data["password"])
            if user is not None:
                login(request,user)
                return HttpResponse("User Loged in ")
                return render(request,"base.html")
            else:
                return HttpResponse("invalid Login ")

    else:
        form = LoginForm()
        return render(request,'users/login.html',{'form':form})
