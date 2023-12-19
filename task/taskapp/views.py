from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Games
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def homepage_content(request):
    data = Games.objects.all()
    return render(request,"index.html",{'content':data})

def login_page(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.athenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login/')

    return render(request,"login.html")

def registration(request):
    if (request.method=='POST'):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists!")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
                messages.info(request,"Created Account Successfully")
                user.save()
                return redirect('login.html')
        else:
            messages.info("Password not matching")
            return redirect('register')                

    return render(request,"register.html")

def browse_content(request):
    return render(request,"browse.html")

def about_content(request): 
    return render(request,"about.html")

def compute_page(request): 
    return render(request,"compute.html")

def contact_content(request):
    return HttpResponse("Contact: 123456789") 

def thanks_content(request): 
    return HttpResponse("Thank you")

def result_content(request):
    x = int(request.GET['number1'])
    y = int(request.GET['number2'])
    add = x+y
    subtract = x-y
    divide = x/y
    multiply = x*y
    return render(request,"result.html",{"addition":add,"subtraction":subtract,"division":divide,"multiplication":multiply})

def logout_page(request):
    auth.logout(request)
    return render(request,'index.html')