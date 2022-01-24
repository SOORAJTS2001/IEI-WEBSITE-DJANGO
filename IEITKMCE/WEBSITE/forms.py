from typing_extensions import Required
from django.db.models import fields
from .models import RegisterModel,Exam1,Exam2,Exam3,AdminLog
from django import forms
from django.forms import ModelForm
from django.core.validators import MinLengthValidator,MaxLengthValidator
class MyRegisterModel(ModelForm):
    Roll_Number= forms.CharField(max_length=100,required=True,
                           widget= forms.TextInput
                           (attrs={'placeholder':'B19EEB..'}))
    Date_Of_Birth = forms.DateTimeField(required=True,
        input_formats=['%d-%m-%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )


    class Meta:
        model = RegisterModel
        
        fields = ['Applicants_Name','Branch_Of_Study','Fathers_Name','Address','Email'
        ,'Mobile_Number','Nationality','Roll_Number','College','Year','Batch','Date_Of_Birth']
class MyExam1(ModelForm):
    class Meta:
        model = Exam1
        fields = ['Exam_Name','Exam_Authority','Register_No','Year_Of_Passing']
class MyExam2(ModelForm):
    class Meta:
        model = Exam2
        fields = ['Exam_Name','Exam_Authority','Register_No','Year_Of_Passing']
class MyExam3(ModelForm):
    class Meta:
        model = Exam3
        fields = ['Exam_Name','Exam_Authority','Register_No','Year_Of_Passing']
class MyAdminLog(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = AdminLog
        fields = ['Username','password']
class MyCertGen(ModelForm):
    class Meta:
        model = AdminLog
        fields = ['Username']


