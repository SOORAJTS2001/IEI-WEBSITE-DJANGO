from typing_extensions import Required
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_mobile(value):
    if len(str(value))!=10:
        raise ValidationError(
            _('It is not a 10 digit mobile number!!'),
            params={'value': value},
        )

def validate_chara(value):
    for val in value:
        if val in ['~','`','!','@','#','%','^','&','*','(',')','{','}','[',']',';',':','?','>','<',',','.','-','_']:
            print("git")
            raise ValidationError(_("Please avoid special characters!!"),params={'value': value},)

            

# Create your models here.
BRANCH = (('EEE','EEE'),('EC','EC'),('MEC','MEC'),('CHEM','CHEM'),('CS','CS'),('MECHPRO','MECHPRO'),('CIVIL','CIVIL'))
YEARS = (("1","1"),("2","2"),("3","3"),("4","4"))
BATCH = (("A","A"),("B","B"),("C","C"),("D","D"))
NAT = (("Indian","Indian"),("Non-Indian","Non-Indian"))
class RegisterModel(models.Model):
  Applicants_Name = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
  Branch_Of_Study = models.CharField(max_length=2500, choices=BRANCH, default='EEE',blank=False)
  Fathers_Name = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
  Address = models.TextField(max_length=2500,blank=False)
  Email = models.EmailField(max_length=2500,blank=False)
  Nationality = models.CharField(max_length=2500,blank=False,choices=NAT,default='Indian')
  College = models.CharField(max_length=2500,blank=False,default="TKM COLLEGE OF ENGINEERING,KOLLAM")
  Year = models.CharField(max_length=2500,blank=False,choices=YEARS,default='1')
  Batch = models.CharField(max_length=2500,blank=False,choices=BATCH,default='A')
  Mobile_Number = models.PositiveBigIntegerField(validators=[validate_mobile],blank=False)
# user_data = {"Name":Name,"Branch":Branch,"Father":Father,"Address":Address,"Email":Email,"Number":Number,"Nationality":Nationality,"Rollno":Rollno,"College":College,"Year":Year,"Batch":Batch,"Date of Birth":Dob,"Exam1":Exam1,'Exam1Auth':Auth1,"Exam1Reg":Regno1,"Yop1":Yop1,"Exam2":Exam2,'Exam2Auth':Auth2,"Exam2Reg":Regno2,"Yop2":Yop2,"Exam3":Exam3,'Exam3Auth':Auth3,"Exam3Reg":Regno3,"Yop3":Yop3}
class Exam1(models.Model):
    Exam_Name = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
    Exam_Authority = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
    Register_No = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
    Year_Of_Passing = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
class Exam2(models.Model):
    Exam_Name = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
    Exam_Authority = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
    Register_No = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
    Year_Of_Passing = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
class Exam3(models.Model):
    Exam_Name = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
    Exam_Authority = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
    Register_No = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
    Year_Of_Passing = models.CharField(max_length=2500,validators=[validate_chara],blank=False)
class AdminLog(models.Model):
    Username = models.CharField(max_length=2500,blank=False)
# from django.core.validators import MaxLengthValidator
class CertGen(models.Model):
    Username = models.CharField(max_length = 2500,validators=[validate_chara],blank=False)