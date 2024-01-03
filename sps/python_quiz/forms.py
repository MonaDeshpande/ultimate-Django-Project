from django import forms
# from django.forms import ModelForm
from .models import administrator_login, administrator_signin, administrator_questions, students_signup, student_signin

class administrator_login_form(forms.ModelForm):
    class Meta:
        model = administrator_login
        # fields = ['firstname', 'lastname', 'admin_id', 'image', 'email_id', 'password', 'reenter_password']
        fields = '__all__'
        labels= { 'firstname': 'First Name', 'lastname': 'Last Name', 'reenter password': 'Re-enter Password'}
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'admin_id':forms.NumberInput(attrs={'class':'form-control'}),
            # 'image':forms.ImageField(attrs={'class':'form-control'}),
            'email_id':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'reenter_password':forms.PasswordInput(attrs={'class':'form-control'})
        }

class administrator_signin_form(forms.ModelForm):
    class Meta:
        model = administrator_signin
        # fields = ['firstname', 'lastname', 'admin_id', 'image', 'email_id', 'password', 'reenter_password']
        fields = '__all__'
        labels= { 'email_id': 'Email Id', 'Password': 'Password'}
        widgets = {
            'email_id':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

class administrator_questions_form(forms.ModelForm):
    class Meta:
        model = administrator_questions
        # fields = ['firstname', 'lastname', 'admin_id', 'image', 'email_id', 'password', 'reenter_password']
        fields = '__all__'
        labels= { 'question': 'Write your question here'}
        widgets = {
            'question':forms.Textarea(attrs={'class':'form-control'}),
        }

class students_signup_form(forms.ModelForm):
    class Meta:
        model = students_signup
        # fields = ['firstname', 'lastname', 'admin_id', 'image', 'email_id', 'password', 'reenter_password']
        fields = '__all__'
        labels= { 'firstname': 'First Name', 'lastname': 'Last Name', 'reenter password': 'Re-enter Password'}
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'student_id':forms.NumberInput(attrs={'class':'form-control'}),
            # 'image':forms.ImageField(attrs={'class':'form-control'}),
            'email_id':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'reenter_password':forms.PasswordInput(attrs={'class':'form-control'})
        }

class student_signin_form(forms.ModelForm):
    class Meta:
        model = student_signin
        # fields = ['firstname', 'lastname', 'admin_id', 'image', 'email_id', 'password', 'reenter_password']
        fields = '__all__'
        labels= { 'email_id': 'Email Id', 'Password': 'Password'}
        widgets = {
            'email_id':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
