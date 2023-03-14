from django.shortcuts import render,HttpResponseRedirect,redirect
from crud.models import Student
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate,login,logout




# Create your views here .  
def logout(request):
    auth.logout(request)
    return redirect('home')

def login(request):
    if request.method == 'POST':
        usern=request.POST['username']
        passw=request.POST['password']
        user=authenticate(username=usern,password=passw)
        if user is not None:  
            return render(request,'app/index.html')
        else:
            messages.info(request,"invalid credential ")
            return redirect('login')
    return render(request,'login.html')



def Registration(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        # password2=request.POST['password2']
        result=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,
                            password=password1)
        
        return render(request,'registration.html',{"result":result})

    return render(request,'registration.html')



def home(request):
    return render(request,'home.html')  
@csrf_protect
@csrf_exempt
def index(request):
    if request.method =='POST':
        student_name=request.POST['name']
        student_surname=request.POST['surname']
        gender=request.POST['gender']
        student_age=request.POST['age']
        contact=request.POST['contact']
        student_address=request.POST['address']
        # if 'hidden' not in request.POST:
        Student.objects.create(name=student_name,surname=student_surname,gender=gender,age=student_age,
                            contact=contact, address=student_address)
        students=Student.objects.all()
        return render(request,'index.html',{'students':students})                   

    students=Student.objects.all()
    return render(request,'index.html',{'students':students})

def show(request):
    students=Student.objects.all()
    return render(request,'show.html',{'students':students})

def Student_list(request):
    students=Student.objects.all()
    return render(request,'index.html', {'students':students})
    
def Student_info(request,sid):
    students=Student.objects.get(id=sid)
    return render(request,'student_info.html',{'students':students})
    
def Student_delete(request,sid):
    Student.objects.get(id=sid).delete()
    students=Student.objects.all()
    return render(request,'index.html',{'students':students})

def Student_update(request, sid):
    stu=Student.objects.get(id=sid)
    if request.method =='POST':
        student_name=request.POST['name']
        student_surname=request.POST['surname']
        gender=request.POST['gender']
        student_age=request.POST['age']
        contact=request.POST['contact']
        student_address=request.POST['address']
        students = Student.objects.filter(id = sid).update(name=student_name,surname=student_surname,gender=gender,age=student_age,
                            contact=contact, address=student_address)
        return render(request,'index.html')
  
    return render(request,'index.html',{'stu':stu})

