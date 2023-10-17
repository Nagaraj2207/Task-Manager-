from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Registration,Task_Manage;
import re

def home(request):
    return render(request, 'home.html')

def user_registration(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname") 
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email_pattern =email_pattern = re.search(r"^[a-z0-9]+([\._]?[a-z0-9]+)*@[a-z]{5}+\.[a-z]{2,3}$",email)
        print(fname)
        print(lname)
        try:
            if not fname.isalpha() or not  lname.isalpha():
                raise Exception ("Name must be in Alphabets")
            elif not email_pattern:
                raise Exception ("Email should be in the correct pattern (Eg:dnagaraj3828@gamil.com)")
            elif password2 != password1:
                raise Exception ("Password and confirm password must be same")
            
            if not Registration.objects.filter(email=email).exists():
                my_data =  Registration(fname = fname,lname = lname,email=email,password=password1)
                my_data.save()
                return redirect(user_login)
            else:
                raise Exception ("This Email is Already Exists")
        except Exception as er:
            error = str(er)
            my_data = {"Error":error}
            print(my_data)
            return render(request,"register.html",context=my_data)

    return render(request, "register.html")

def user_login(request):
    global email
    if request.method == "POST":
        email = request.POST.get("email")
        password= request.POST.get("password")
        if Registration.objects.filter(email=email,password=password).exists():
            return redirect(task_app_home)
        else:
            error = "Please Enter the Correct Email or Password"
            my_data = {"Error":error}
            return render(request,"login.html",context=my_data)
    
    return render(request, "login.html")


def forget_pass(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if Registration.objects.filter(email=email).exists():
            password1= request.POST.get("password1")
            password2= request.POST.get("password2")
            if password1 == password2:
                Registration.objects.filter(email=email).update(password=password1)
                return redirect(user_login)
            else:
                error = "New Password and confirm password are not same!!!"
                my_data = {"Error":error}
                return render(request,"forgot_password.html",context=my_data)                
        else:
            error = "Please Enter the correct Email"
            my_data = {"Error":error}
            return render(request,"forgot_password.html",context=my_data)    
    return render(request, "forgot_password.html")


def task_app_home(request):
    user = Registration.objects.filter(email=email)
    tasks = Task_Manage.objects.filter(user=email)
    completed_count = tasks.filter(completed='yes').aggregate(completed_count=Count('id'))
    not_completed_count = tasks.filter(completed='no').aggregate(not_completed_count=Count('id'))
    all_data = tasks.aggregate(all_data=Count('id'))
    my_data ={"User":user,"All_data":all_data,"Completed":completed_count,"NotCompleted":not_completed_count}
    return render(request,"task_app_home.html",context=my_data)

def update_user(request):
    user_data = Registration.objects.filter(email=email)
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname") 
        try:
            if not fname.isalpha() or not  lname.isalpha():
                raise Exception ("Name must be in Alphabets")
            Registration.objects.filter(email=email).update(fname=fname,lname=lname)
            return redirect(task_app_home)
        except Exception as er:
            error = str(er)
            my_data = {"Error": error}
            return render(request,"update_user.html",context=my_data)
    return render(request,"update_user.html",{"User_data":user_data})

def change_password(request):
    if request.method == "POST":
        curpass = request.POST.get("curpass")
        if Registration.objects.filter(password=curpass).exists():
            password1= request.POST.get("password1")
            password2= request.POST.get("password2")
            if password1 == password2:
                Registration.objects.filter(email=email).update(password=password1)
                return redirect(task_app_home)
            else:
                error = "New Password and confirm password are not same!!!"
                my_data = {"Error":error}
                return render(request,"change_pass.html",context=my_data)                
        else:
            error = "Please Enter the correct Email"
            my_data = {"Error":error}
            return render(request,"change_pass.html",context=my_data)    
    return render(request, "change_pass.html")


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get("title") 
        title = title.upper()
        description = request.POST.get("description")
        completed = request.POST.get("completed")
        due_date = request.POST.get("due_date")
        priority = request.POST.get("priority")
        try:
            if not title.isalpha and not description.isalpha:
                raise Exception ("Title and Description must be in Alphabets")
        except Exception as er:
            error = str(er)
            my_data = {"Error":error}
            return render(request, "app_task.html",context=my_data)
        
        user_registration = Registration.objects.get(email=email)

        if not Task_Manage.objects.filter(title=title).exists():
            add_tasks = Task_Manage(user=user_registration,title=title, description=description, completed=completed, due_date=due_date, priority=priority)
            add_tasks.save()
            message="Task added successfully!"
            my_data = {"Message":message}
            return render(request,"add_task.html",context=my_data)
        else:
            error = "Task already exists!!!"
            my_data = {"Error":error}
            return render(request,"add_task.html",context=my_data) 
    return render(request,"add_task.html")


def view_task(request):
    sort = request.GET.get('sort')
    query = request.GET.get("query")
    tasks = Task_Manage.objects.filter(user=email)
    if sort == 'priority':
        tasks = tasks.order_by('priority')
    elif sort == 'due_date':
        tasks = tasks.order_by('due_date')
    elif query != None:
        tasks = tasks.filter(title__icontains=query)
    
    return render(request,"view_task.html",{'tasks':tasks})


def update_task(request,id):
    tasks = Task_Manage.objects.filter(user=email,id=id)
    my_task = {'tasks':tasks}
    if request.method == 'POST':
        completed = request.POST.get("completed")
        Task_Manage.objects.filter(id=id).update(completed=completed)
        return redirect(view_task)
    return render(request,"update_task.html",context=my_task)


def delete_task(request,id):
    tasks = Task_Manage.objects.filter(user=email,id=id)
    my_data = {"tasks":tasks}
    if request.method == 'POST':
        my_task = Task_Manage.objects.filter(id=id)
        my_task.delete()
        return redirect(view_task)
    return render(request,"delete_task.html",context=my_data)