from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm,CowForm
from myapp.models import Cow
from myapp.functions import handle_uploaded_file
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

def user_dashboard(request):
	return render(request, 'dashboard.html')
# Create your views here.
def add_cow(request):
    form = CowForm()
    if request.method == "POST":
        form = CowForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard')
    return render(request,'add_cow.html',{'form':form})
			

def list_cow(request):
    all_cows = Cow.objects.all()
    context = {'all_cows':all_cows}
    return render(request,'dashboard.html',context)


def contactPage(request):
    return render(request, 'contacts.html')

def aboutPage(request):
    return render(request, 'about.html')

def deleteCow(request,pk):
    cow = Cow.objects.get(id=pk)
    if request.method == 'POST':
        cow.delete()
        return redirect('dashboard')
    return render(request,'delete.html',{'obj':cow})

def updateCow(request,pk):
    cow = Cow.objects.get(id=pk)
    form = CowForm(instance=cow)

    if request.method == 'POST':
        form = CowForm(request.POST,instance=cow)
        if form.is_valid():
            form.save()
            return  redirect('dashboard')
    context = {'form':form}
    return render(request,'cow_form.html',context)