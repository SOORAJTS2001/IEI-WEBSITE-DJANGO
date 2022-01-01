from typing_extensions import Required
from django.db import models
from django import forms

# Create your models here.
BRANCH = (('EEE','EEE'),('EC','EC'),('MEC','MEC'),('CHEM','CHEM'),('CS','CS'),('MECHPRO','MECHPRO'),('CIVIL','CIVIL'))
YEARS = (("1","1"),("2","2"),("3","3"),("4","4"))
class RegisterModel(models.Model):
  Name = models.CharField(max_length=2500,blank=False)
  Branch = models.CharField(max_length=2500, choices=BRANCH, default='EEE',blank=False)
  Father = models.CharField(max_length=2500,blank=False)
  Address = models.TextField(max_length=2500,blank=False)
  Email = models.CharField(max_length=2500,blank=False)
  Number = models.CharField(max_length=2500,blank=False)
  Nationality = models.CharField(max_length=2500,blank=False)
  College = models.CharField(max_length=2500,blank=False)
  Year = models.CharField(max_length=2500,blank=False,choices=YEARS,default='1')
class Exam1(models.Model):
    Exam = models.CharField(max_length=2500,blank=False)
    Authority = models.CharField(max_length=2500,blank=False)
    Regno = models.CharField(max_length=2500,blank=False)
    YearofPassing = models.CharField(max_length=2500,blank=False)
class Exam2(models.Model):
    Exam = models.CharField(max_length=2500,blank=False)
    Authority = models.CharField(max_length=2500,blank=False)
    Regno = models.CharField(max_length=2500,blank=False)
    YearofPassing = models.CharField(max_length=2500,blank=False)
class Exam3(models.Model):
    Exam = models.CharField(max_length=2500,blank=False)
    Authority = models.CharField(max_length=2500,blank=False)
    Regno = models.CharField(max_length=2500,blank=False)
    YearofPassing = models.CharField(max_length=2500,blank=False)
class AdminLog(models.Model):
    Username = models.CharField(max_length=2500,blank=False)
class CertGen(models.Model):
    Username = models.CharField(max_length=2500,blank=False)