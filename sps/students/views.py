from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Students

def students_home(request):
    students = Students.objects.all()
    #will bring student in dictionary
    return render(request, "students/home.html", {
        'students':students
    })

def students_data(request):
    return render (request, "students/students_data.html", {})

def add_students(request):
     global phy
     global chem
     global bio
     global maths
     if request.method =="POST":
        #print("data is coming")
        #fetch data
        student_firstname = request.POST.get("firstname")
        student_lastname = request.POST.get("lastname")
        student_id = request.POST.get("student_id")
        phy = request.POST.get("phy")
        chem = request.POST.get("chem")
        bio = request.POST.get("bio")
        maths = request.POST.get("maths")

        def percentage(a, b, c):
            percentage= ((int(a)+int(b)+int(c))/3)
            return percentage
        
        pcb = percentage(phy, chem, bio)
        pcm = percentage(phy, chem, maths)
        
        data ={"pcm": pcm,
               "pcb": pcb,
               }
        print(student_id)

        #Create model object and set data
        s=Students()
        s.firstname =student_firstname
        s.lastname = student_lastname
        s.student_id = student_id
        s.phy=phy
        s.chem =chem
        s.maths =maths
        s.bio =bio
        s.pcb = pcb
        s.pcm =pcm

        #save data
        s.save()
        return redirect ("/students/home/")
     
     print("data is not coming")
     return render(request, "students/add_student.html", {})

def delete_student(request, student_id):
    print(student_id)
    x=Students.objects.get(pk=student_id)
    print(x)
    x.delete()
    return redirect("/students/home/")

def update_student(request, student_id):
    students = Students.objects.get(pk=student_id)
    print("update the data of this student")
    return render(request, "students/update.html", {
        'students':students
    })
    
def do_update(request, student_id):
    if request.method =="POST":
        #print("data is coming")
        #fetch data
        student_firstname = request.POST.get("firstname")
        student_lastname = request.POST.get("lastname")
        student_id_temp = request.POST.get("student_id")
        phy = request.POST.get("phy")
        chem = request.POST.get("chem")
        bio = request.POST.get("bio")
        maths = request.POST.get("maths")

        def percentage(a, b, c):
            percentage= ((int(a)+int(b)+int(c))/3)
            return percentage
        
        pcb = percentage(phy, chem, bio)
        pcm = percentage(phy, chem, maths)
        
        data ={"pcm": pcm,
               "pcb": pcb,
               }
        print(student_id)

        print(student_id)

        s = Students.objects.get(pk=student_id)

        #Create model object and set data
        s.firstname =student_firstname
        s.lastname = student_lastname
        s.student_id = student_id_temp
        s.phy=phy
        s.chem =chem
        s.maths =maths
        s.bio =bio
        s.pcb = pcb
        s.pcm =pcm

        #save data
        s.save()
    
    return redirect("/students/home/")
    


