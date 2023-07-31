from django.shortcuts import render

# Create your views here.
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
#venv\scripts\activate
def home(request):
       
    return render(request, 'home.html')
def packages(request):
       
    return render(request, 'packages.html')
def services(request):
       
    return render(request, 'services.html')