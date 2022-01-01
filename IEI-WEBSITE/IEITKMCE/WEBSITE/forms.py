from typing_extensions import Required
from django.db.models import fields
from .models import CertGen, RegisterModel,Exam1,Exam2,Exam3,AdminLog
from django import forms
from django.forms import ModelForm
class MyRegisterModel(ModelForm):
    Rollno= forms.CharField(max_length=100,required=True,
                           widget= forms.TextInput
                           (attrs={'placeholder':'B19EEB..'}))
    Dob = forms.DateTimeField(required=True,
        input_formats=['%d-%m-%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

    class Meta:
        model = RegisterModel
        
        fields = ['Name','Branch','Father','Address','Email'
        ,'Number','Nationality','Rollno','College','Year','Dob']
class MyExam1(ModelForm):
    class Meta:
        model = Exam1
        fields = ['Exam','Authority','Regno','YearofPassing']
class MyExam2(ModelForm):
    class Meta:
        model = Exam2
        fields = ['Exam','Authority','Regno','YearofPassing']
class MyExam3(ModelForm):
    class Meta:
        model = Exam3
        fields = ['Exam','Authority','Regno','YearofPassing']
class MyAdminLog(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = AdminLog
        fields = ['Username','password']
class MyCertGen(ModelForm):
    class Meta:
        model = AdminLog
        fields = ['Username']


