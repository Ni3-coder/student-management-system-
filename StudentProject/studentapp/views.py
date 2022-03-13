from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from studentapp.forms import Add_School_Form, Add_Student_Form
from django.contrib.auth.decorators import login_required

from studentapp.models import School, Student


@login_required
def home(request):
    return render(request, "studentapp/home.html")


def create_account(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'studentapp/createaccount.html',{'form':form})


@login_required
def addstudent(request):
    form = Add_Student_Form()
    if request.method == "POST":
        form = Add_Student_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list/')
    return render(request,'studentapp/addstudent.html',{'form':form})


@login_required
def update_student(request,id):
    obj = Student.objects.get(pk=id)
    form = Add_Student_Form(instance=obj)
    if request.method == 'POST':
        form = Add_Student_Form(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/list/')
    return render(request, 'studentapp/addstudent.html',{'form':form})


@login_required
def add_school(request):
    form = Add_School_Form()
    if request.method == "POST":
        form = Add_School_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list/')
    return render(request,'studentapp/addschool.html',{'form':form})


@login_required
def list(request):
    obj = Student.objects.all()
    return render(request,'studentapp/list.html',{'obj':obj})


@login_required
def details(request, id):
    obj = Student.objects.get(pk = id)
    return render(request,'studentapp/details.html',{'obj':obj})


@login_required
def delete(request,id):
    obj = Student.objects.get(pk = id)
    obj.delete()
    return redirect('/list/')