from django.db import models

# Create your models here.
class administrator_login(models.Model):
    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=False)
    admin_id = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to="administrator_login/", blank=True)
    email_id = models.EmailField(blank=True, primary_key= True)
    password = models.CharField(max_length=100, null=False)
    reenter_password = models.CharField(max_length=100, null=False)
    

    def __str__(self):
        return self.firstname
    
class administrator_signin(models.Model):
    email_id = models.EmailField(blank=True, primary_key = True)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.email_id

class administrator_questions(models.Model):
    id =models.IntegerField(default=None, primary_key=True, null=False)
    question = models.CharField(max_length=500, default=None)
    option_A = models.CharField(max_length=100, null=False)
    option_B = models.CharField(max_length=100, null=False)
    option_C = models.CharField(max_length=100, null=False)
    option_D = models.CharField(max_length=100, null=False)
    correct_answer = models.CharField(max_length=100, null = False)

    def __str__(self):
        return self.question

class students_signup(models.Model):
    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=False)
    student_id = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to="administrator_login/", blank=True)
    email_id = models.EmailField(blank=True, primary_key= True)
    password = models.CharField(max_length=100, null=False)
    reenter_password = models.CharField(max_length=100, null=False)
    

    def __str__(self):
        return self.firstname

class student_signin(models.Model):
    email_id = models.EmailField(blank=True, primary_key = True)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.email_id