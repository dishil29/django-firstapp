from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url= '/login/')
def home(request):

  return render(request , 'home.html')

@login_required(login_url= '/login/')
def default(request):
  return render(request , 'home.html')


def login_page(request):
  if request.method == "POST":
    data = request.POST
    username = data.get("email")
    password  = data.get('password')

    if User.objects.filter(username = username).exists():
      user = authenticate(username = username, password = password)
      if user is None:
        messages.error(request, 'Invalid password')
        return redirect('/login/')
      else:
        login(request , user)
        return redirect('/home/')
    else :
      messages.error(request, 'Invalid username')
      return redirect('/login/')
  return render(request, 'login.html')

def register(request):
  if request.method == "POST":
    data = request.POST
    email = data.get('email')
    name = data.get("name")
    password = data.get("password")

    user = User.objects.filter(username = email)
    if user.exists():
      messages.info(request, "Email already registered")
      return redirect('/register/')

    user = User.objects.create( username=email, first_name = name )
    user.set_password(password)
    user.save()

    messages.info(request, "Account created successfully")
    
    return redirect('/register/')
  return render(request, 'register.html')