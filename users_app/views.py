from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
    context = {
        'user' : User.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    age = request.POST['age']
    User.objects.create(
        first_name = fname, 
        last_name = lname, 
        email_address = email, 
        age = age)
    return redirect('/')

