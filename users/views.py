from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth import
# from SocialMedia.users.forms import LoginForm   # another way below 
from .forms import LoginForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data["username"], password=data["password"])
            if user is not None: 
                login(request,user)
                return HttpResponse("User Loged in ")
                
            else:
                return HttpResponse("invalid Login ")

    else:
        form = LoginForm()
        return render(request,'users/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return render(request,'users/logout.html')

@login_required
def index(request):
    return render(request,'users/index.html')


def password_change(request):

    return render(request,'users/password_change_form.html')


def registor(request):
    if request.method=='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'users/registor_done.html')

    else:
        user_form= UserRegistrationForm()
    return render(request,'users/registor.html',{'user_form':user_form})

