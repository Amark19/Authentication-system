from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import logout,authenticate,login
# Create your views here.
#amar
#Pass@123
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
        print("wrong")
    
    return render(request,'index.html')
def loginUser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print("hi")
            return redirect('/')
            
        else:
            return render (request,'login.html')
            print("wrong")
    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return redirect("/login")
    #pass=Amar9930%