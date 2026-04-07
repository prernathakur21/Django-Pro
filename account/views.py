from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from .models import Employee


# Create your views here.

def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method =='POST':
        # name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
        # name=name,
        username=username,
        email=email,
        password=password
    )
    return render(request,'signup.html')

def welcome(request):
    return render(request,'welcome.html')

def add(request):
    return render(request,'add.html')
    
    
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get ('password')
        user=authenticate(request,
          username=username,
          password=password
        )
        if user is not None:
            return redirect("welcome")
        else:
            messages.error(request,"Invalid Password or Username or Complete your signup process")
            return render(request,'signin.html')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request,"LogOut successful")
    return redirect("signin")

def add(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        salary = request.POST.get('salary')
        age = request.POST.get('age')
        city = request.POST.get('city')

        Employee.objects.create(
            name=name,
            salary=salary,
            age=age,
            city=city
        )
        return redirect('/view')
    return render(request, 'add.html')

def index(request):
    employee=Employee.objects.all()
    return render(request,'index.html', {'employee':employee})

def delete(request, id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/view')

def update(request, id):
    emp=Employee.objects.get(id=id)

    if request.method=='POST':
        emp.name = request.POST.get('name')
        emp.salary = request.POST.get('salary')
        emp.age = request.POST.get('age')
        emp.city = request.POST.get('city')
        
        emp.save()
        return redirect('/view')
    return render(request,'update.html', {'emp':emp})




