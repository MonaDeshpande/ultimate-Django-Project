from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import *
from .forms import administrator_login_form, administrator_signin_form,students_signup_form,student_signin_form
from .models import administrator_login,administrator_signin, administrator_questions,students_signup,student_signin
# from django.views import View
#create a list to keep the record of question id
question_id =[1, 3, 4]

# Create your views here.

def home(request):
    Administrator_login= administrator_login.objects.all()
    #will bring student in dictionary
    return render(request, "python_quiz/home.html", {
        'administrator_login': Administrator_login
    })
    return render (request, "python_quiz/home.html", {})


def admin_login(request):

    form = administrator_login_form()
  
    if request.method =="POST":
        form = administrator_login_form(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'python_quiz/admin_signup.html', context)
    

def admin_details(request):
    administrator_details = administrator_login.objects.all
    return render (request, "python_quiz/admin_details.html", {'administrator_details': administrator_details})

def delete_admin(request, email_id):
    print(email_id)
    x=administrator_login.objects.get(email_id=email_id)
    print(x)
    x.delete()
    return redirect("/python_quiz/home/")

def update_admin(request, email_id):
    data = administrator_login.objects.get(email_id=email_id)
    form = administrator_login_form(instance=data)

    if request.method =="POST":
        form = administrator_login_form(request.POST, instance=data)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'python_quiz/admin_login.html', context)

def sign_in(request):
    form = administrator_signin_form()
  
    if request.method =="POST":
        form = administrator_signin_form(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}   
    return render(request, 'python_quiz/admin_signin.html', context)


def add_questions(request):
    if request.method =="POST":
        email_id1 = request.POST.get("email_id")
        password1 = request.POST.get("password")
        AL= administrator_login

        try:
            whole_Details = AL.objects.get(email_id = email_id1)
        except:
            HttpResponse("Enter correct email address")

        email_id2 = whole_Details.email_id
        password2 = whole_Details.password

        if email_id1 == email_id2 and password1 == password2:
            return render(request, "python_quiz/questions.html", {})
        else:
            return HttpResponse("Email id or password doesn't match")

def questions(request):
    if request.method =="POST":
        id = request.POST.get("id")
        Question = request.POST.get("question")
        Option_A = request.POST.get("option_A")
        Option_B = request.POST.get("option_B")
        Option_C = request.POST.get("option_C")
        Option_D = request.POST.get("option_D")
        Correct_Answer = request.POST.get("correct_answer")

        # Create model object and save data
        Q=administrator_questions()
        Q.id= id
        Q.question = Question
        Q.option_A = Option_A
        Q.option_B = Option_B
        Q.option_C = Option_C
        Q.option_D = Option_D
        Q.correct_answer = Correct_Answer
        #save data
        Q.save()

        question_id.append[id]

        return redirect ("/python_quiz/questions/")
    print("data is not coming")
    return render(request, "python_quiz/questions.html", {})

def question_details(request):
    #return HttpResponse("Hello its working")
    question_details = administrator_questions.objects.all
    return render (request, "python_quiz/question_details.html", {'question_details': question_details})

def delete_question(request, id):
    print(id)
    # return HttpResponse(question)
    x=administrator_questions.objects.get(pk= id)
    print(x)
    x.delete()
    return redirect("/python_quiz/question_details/")

def update_question(request, id):
    x = administrator_questions.objects.get(pk=id)
    # return HttpResponse(x.question)
    return render(request, "python_quiz/questions_update.html", {'administrator_question':x})

def do_update_question(request, id):
    if request.method =="POST":
        Question = request.POST.get("question")
        Option_A = request.POST.get("option_A")
        Option_B = request.POST.get("option_B")
        Option_C = request.POST.get("option_C")
        Option_D = request.POST.get("option_D")
        Correct_Answer = request.POST.get("correct_answer")

        # Create model object and save data
        Q=administrator_questions()
        Q.id= id
        Q.question = Question
        Q.option_A = Option_A
        Q.option_B = Option_B
        Q.option_C = Option_C
        Q.option_D = Option_D
        Q.correct_answer = Correct_Answer

        #save data
        Q.save()

        return redirect ("/python_quiz/questions/")
    print("data is not coming")
    return render(request, "python_quiz/questions.html", {})

def student_signup(request):

    form = students_signup_form()
  
    if request.method =="POST":
        form = students_signup_form(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'python_quiz/student_signup.html', context)
    
def student_details(request):
    student_details = students_signup.objects.all()
    return render (request, "python_quiz/student_details.html", {'student_details': student_details})

def delete_student(request, email_id):
    print(email_id)
    x=student_signup.objects.get(email_id=email_id)
    print(x)
    x.delete()
    return redirect("/python_quiz/home/")

def update_student(request, email_id):
    #return HttpResponse("done")
    data = students_signup.objects.get(email_id=email_id)
    form = students_signup_form(instance=data)

    if request.method =="POST":
        form = students_signup_form(request.POST, instance=data)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'python_quiz/student_signup.html', context)

def signin_student(request):
    form = student_signin_form()
  
    if request.method =="POST":
        form = student_signin_form(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}   
    return render(request, 'python_quiz/student_signin.html', context)
# def random_question(request):
#     que_id = administrator_questions.objects.filter().values_list('id', flat=True)
#     import random
#     que_to_display = random.choice(que_id)
#     que =administrator_questions.objects.get(pk=que_to_display)
#     # return HttpResponse(x)
#     return render(request, "python_quiz/exam.html", {'que': que})
def random_question(request):
    global que_id
    global whole_details
    global que
    global options
    que_id = administrator_questions.objects.filter().values_list('id', flat=True)
    import random
    que_to_display = random.choice(que_id)
    whole_details =administrator_questions.objects.get(pk=que_to_display)
    que = whole_details.question
    options ={
        "A" :whole_details.option_A,
        "B" : whole_details.option_B,
        "C" : whole_details.option_C,
        "D" : whole_details.option_D
    }
    
    context = {
        'que': que,
        'options':options
        }
        
    return render(request, "python_quiz/questionnaire.html", context)

def selected_answer(request):
    if request.method =="POST":
        if request.POST.get('options'):
            vi= request.POST.get('options')
            print(vi)
            vi = str(vi)
                # return HttpResponse(vi)
        
            right_ans = whole_details.correct_answer
            if vi ==right_ans:
                result= "Your answer is right"
            else:
                result = "Your answer is wrong"
            context = {
                'que': que,
                'options':options,
                'result':result
                }
            return render(request, "python_quiz/questionnaire.html", context)
        else:
            return redirect("/python_quiz/random_question/")
            
            
       
        # selected_option = request.POST.getlist('options')
        # if selected_option =="A" and correct_answer =="A":
        #     result ="Your answer is right"
        #     # return HttpResponse(result)
        # elif selected_option =="B" and correct_answer =="B":
        #     result ="Your answer is right"
        #     # return HttpResponse(result)
        # elif selected_option =="C" and correct_answer =="C":
        #     result ="Your answer is right"
        #     # return HttpResponse(result)
        # elif selected_option =="D" and correct_answer =="D":
        #     result ="Your answer is right"
        #     # return HttpResponse(result)
        # else:
        #     result ="Your answer is right"
        #     # return HttpResponse(result)
    
def exam(request):
    question= administrator_questions.objects.all()
    
    # import random
    # que= random.randint(1, question.id)
    return HttpResponse(question)
    # question = administrator_questions.objects.get(pk=que)
    # return HttpResponse(question)


        


    
    
    
    
        