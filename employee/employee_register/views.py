from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages 


# Create your views here.
def index(request):
    #we are retriving data which is submitted in form and getting data from backend and showing in console by {{d.id}} in this way which is written in index.html

    data=Student.objects.all()
    context={"data":data}
    return render(request,"index.html",context)
def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data is Updated")#this is to show message on console
        return redirect("/")
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"update.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.error(request,"Data is Deleted")

    return redirect("/")

def insertData(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data Inserted Successfully") #this for user experience to see data is updated or deleted and written in index.html in for loop after student details 
        return redirect("/")
    return render(request,"index.html")
