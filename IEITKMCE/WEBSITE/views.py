from unicodedata import name
from django.shortcuts import render,redirect#it is used for redirection and rendering webpage in a html page
from .forms import MyRegisterModel,MyExam1,MyExam2,MyExam3,MyAdminLog,MyCertGen#form models for iei new registrations with their exam data,with certificate generator
from django.contrib import messages#to display messages in html in alert colors
from . import firebase#relative import to the firebase module
from django.http import HttpResponse#to import http response
from datetime import datetime#it is to generate the random code for individual registration
firebase1 =firebase.FirebaseApplication('https://ieitkmce-default-rtdb.firebaseio.com/', None)  
from django.contrib.auth.decorators import login_required
from django.http import FileResponse#To return generated PDF file 
from django.contrib.auth import authenticate, login, logout#it is to authenticate the User sett as admin,note:@login required can only used for that
from PyPDF2 import PdfFileWriter, PdfFileReader#it generates the modified pdf
import io,csv#to generate the buffer
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import yagmail
def send_mail_dic(data_dic,subjects,email):
    try:
        #initializing the server connection
        yag = yagmail.SMTP(user='dpservice200@gmail.com', password='Soorajsivadas767')
        #sending the email
        #user_data = {"Name":Name,"Branch":Branch,"Father":Father,"Address":Address,"Email":Email,"Number":Number,"Nationality":Nationality,"Rollno":Rollno,"College":College,"Year":Year,"Batch":Batch,"Date of Birth":Dob,"Exam1":Exam1,'Exam1Auth':Auth1,"Exam1Reg":Regno1,"Yop1":Yop1,"Exam2":Exam2,'Exam2Auth':Auth2,"Exam2Reg":Regno2,"Yop2":Yop2,"Exam3":Exam3,'Exam3Auth':Auth3,"Exam3Reg":Regno3,"Yop3":Yop3}

        yag.send(to=email, subject=subjects, contents=f'''<h3>
        Hi {data_dic['Name']},Thank you for showing interest in IEI TKMCE!,
        </h3>
        <br>
        We got your details as follows..
        Name                   : <b>{data_dic['Name']}</b>
        Father's name          : <b>{data_dic['Father']}</b>
        Roll Number             :<b>{data_dic['Rollno']}</b>
        Batch                  : <b>{data_dic['Batch']}</b>
        Branch                 : <b>{data_dic['Branch']}</b>
        Year                  : <b>{data_dic['Year']}</b>
        College                 : <b>{data_dic['College']}</b>
        Email                   : <b>{data_dic['Email']}</b>
        Mobile number              : <b>{data_dic['Number']}</b>
        Date of Birth                 : <b>{data_dic['Date of Birth']}</b>
        
        <b>If you want to change the data,please resubmit the form with your given email address and <br>
        mobile number</b>
        <b>Please don't reply to this machine generated mail!!!</b>
        Regards Web Team,IEI TKMCE
        Any doubt?? <a href="https://wa.me/916282143473?text=Hello Sooraj,I have a doubt..">Contact me!</a>
        ''')
        return True
    except:
        return False

def error_404(request, exception):
    return render(request,"404.html",status=404)
def error_403(request, exception):
    return render(request,"403.html",status=403)
def error_500(request,*args, **argv):
    return render(request,"500.html",status=500)
def error_400(request, exception):
    return render(request,"400.html",status=400)
def home(request):
    return render(request,'WEBSITE/index.html')
def register(request):
# datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%H%M%S")#generating the random code for user identification 
    print("date and time =", dt_string)
    
    if request.method == "GET":
        form = MyRegisterModel()
        exam_form1 = MyExam1()
        exam_form2 = MyExam2()
        exam_form3 = MyExam3()
    else:
        form = MyRegisterModel(request.POST)
        exam_form1 = MyExam1(request.POST)
        exam_form2 = MyExam2(request.POST)
        exam_form3 = MyExam3(request.POST)
        if form.is_valid() and exam_form1.is_valid() and exam_form2.is_valid() and exam_form3.is_valid():#checking validity
            Name = form.cleaned_data['Applicants_Name']
            Branch = form.cleaned_data['Branch_Of_Study']
            Father = form.cleaned_data['Fathers_Name']
            Address = form.cleaned_data['Address']
            Email = form.cleaned_data['Email']
            Number = form.cleaned_data['Mobile_Number']
            Nationality = form.cleaned_data['Nationality']
            Rollno = form.cleaned_data['Roll_Number']
            College = form.cleaned_data['College']
            Year = form.cleaned_data['Year']
            Dob = form.cleaned_data['Date_Of_Birth']
            Batch = form.cleaned_data['Batch']
            print(type(Dob))
            Dob = Dob.strftime("%d/%m/%Y")#changing the dob to required type
            Exam1 = exam_form1.cleaned_data['Exam_Name']
            Auth1 = exam_form1.cleaned_data['Exam_Authority']
            Regno1 = exam_form1.cleaned_data['Register_No']
            Yop1 = exam_form1.cleaned_data['Year_Of_Passing']

            Exam2 = exam_form2.cleaned_data['Exam_Name']
            Auth2 = exam_form2.cleaned_data['Exam_Authority']
            Regno2 = exam_form2.cleaned_data['Register_No']
            Yop2 = exam_form2.cleaned_data['Year_Of_Passing']

            Exam3 = exam_form3.cleaned_data['Exam_Name']
            Auth3 = exam_form3.cleaned_data['Exam_Authority']
            Regno3 = exam_form3.cleaned_data['Register_No']
            Yop3 = exam_form3.cleaned_data['Year_Of_Passing']
            data_firebase = firebase1.get('/REGISTRATION','')
            found = True
            result = ""
            for key,value in data_firebase.items():
                data_dic = eval(value)
                if Email == data_dic['Email'] and Number == data_dic['Number']:
                    user_data = {"Name":Name,"Branch":Branch,"Father":Father,"Address":Address,"Email":Email,"Number":Number,"Nationality":Nationality,"Rollno":Rollno,"College":College,"Year":Year,"Batch":Batch,"Date of Birth":Dob,"Exam1":Exam1,'Exam1Auth':Auth1,"Exam1Reg":Regno1,"Yop1":Yop1,"Exam2":Exam2,'Exam2Auth':Auth2,"Exam2Reg":Regno2,"Yop2":Yop2,"Exam3":Exam3,'Exam3Auth':Auth3,"Exam3Reg":Regno3,"Yop3":Yop3}
                    result = firebase1.put('/REGISTRATION',key,str(user_data))
                    if send_mail_dic(data_dic,"IEI Registration Resubmission Succesfull!",Email):
                        messages.success(request,f"Your form has been resubmitted,Now Please check you registered email!!")
                    else:
                        messages.info(request,"Hey are you sure this is a valid email address?..since we can't find the address")
                    found = True
                    break
                elif Email == data_dic['Email'] and Number != data_dic['Number']:
                    found = True
                    messages.warning(request,f"Your email {Email} has been registered with your Number already,please provide the same to resubmit the form!")
                    break
                elif Email != data_dic['Email'] and Number == data_dic['Number']:
                    found = True
                    messages.warning(request,f"Your Mobile number {Number} has been registered with your Email already,please provide the same to resubmit the form!")
                    break
                else:
                    found = False
            if found == False:
                user_data = {"Name":Name,"Branch":Branch,"Father":Father,"Address":Address,"Email":Email,"Number":Number,"Nationality":Nationality,"Rollno":Rollno,"College":College,"Year":Year,"Batch":Batch,"Date of Birth":Dob,"Exam1":Exam1,'Exam1Auth':Auth1,"Exam1Reg":Regno1,"Yop1":Yop1,"Exam2":Exam2,'Exam2Auth':Auth2,"Exam2Reg":Regno2,"Yop2":Yop2,"Exam3":Exam3,'Exam3Auth':Auth3,"Exam3Reg":Regno3,"Yop3":Yop3}
                send_mail_dic(user_data,"IEI Registration Succesfull",Email)
                if send_mail_dic(data_dic,"IEI Registration Resubmission Succesfull!",Email):
                    messages.success(request,f"Thank you {Name} for showing interest in IEI TKMCE,Please check your registered email")
                else:
                    messages.success(request,f"Thank you {Name} for showing interest in IEI TKMCE,Please check your registered email")
                result = firebase1.put('/REGISTRATION',dt_string,str(user_data))
            return redirect('register')
        else:
           messages.warning(request,"Hey! Make sure you have given details correctly..")
    return render(request,'WEBSITE/register.html',{"form":form,"exam_form1":exam_form1,"exam_form2":exam_form2,"exam_form3":exam_form3})

def admin_login(request):
    admins = firebase1.get('Admin/','')
    if request.method == 'GET':
        form = MyAdminLog()
    else:
        form = MyAdminLog(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['Username']
            Password = form.cleaned_data['password']
            print(admins)
            print(Username)
            print(Password)
          # messages.success(request,"Successfully logged in ")
            user = authenticate(request, username=Username, password=Password)#trying to authenticate the User with admin user
            if user is not None:
                login(request, user)#logging in the user
                messages.success(request,"Successfully logged in ")
                return redirect('admin-page')       
            else:
                messages.warning(request,"Username/Password not correct")
                return redirect('admin-login')
    return render (request,'WEBSITE/admin-login.html',{"form":form})
@login_required(login_url="admin-login")#the user has to bypass the admin-login
def admin_page(request):
    data = []
    count = 0
    Logout = request.POST.get('logout','false')
    if Logout!= "false":
        logout(request)#to logout the user
        messages.warning(request,"You have been logged out!")
        return redirect("index")
    data_firebase = firebase1.get('/REGISTRATION','')
    for key,value in data_firebase.items():
        data_dic = eval(value)
        data.append(data_dic['Name']+'-'+key)
        print(key)
        count+=1#to print the number of registration
    Export_as_csv= request.POST.get('export_as_csv','false')
    Code = request.POST.get('button','false')
    print(Code)
    if Code!="false":
        code = Code.split('-')[1]
        if code in data_firebase:
            data_dic = eval(data_firebase[code])
            Name = data_dic['Name']
            Branch = data_dic['Branch']
            Father = data_dic['Father']
            Address = data_dic['Address']
            Email = data_dic['Email']
            Number = str(data_dic['Number'])
            Nationality = data_dic['Nationality']
            Rollno = data_dic['Rollno']
            College = data_dic['College']
            Year = data_dic['Year']
            Dob = data_dic['Date of Birth']
            Batch = data_dic['Batch']

            Exam1 = data_dic['Exam1']
            Auth1 = data_dic['Exam1Auth']
            Regno1 = data_dic['Exam1Reg']
            Yop1 = data_dic['Yop1']

            Exam2 = data_dic['Exam2']
            Auth2 = data_dic['Exam2Auth']
            Regno2 = data_dic['Exam2Reg']
            Yop2 = data_dic['Yop2']

            Exam3 = data_dic['Exam3']
            Auth3 = data_dic['Exam3Auth']
            Regno3 = data_dic['Exam3Reg']
            Yop3 = data_dic['Yop3']
            filename = f"{Name}-{code}-IEI-REGISTRATION.txt"#registration form
            content = f"""
                                            IEI REGISTRATION FORM \n
                                            ----------------------
    Student details 

Name                            : {Name} 
Year of study                   : {Year}    
Branch                          : {Branch}
Batch                           : {Batch}
Father's name                   : {Father}
Address                         : {Address}
Email                           : {Email}
Number                          : {Number}
Nationality                     : {Nationality}
Rollno                          : {Rollno}
College                         : {College}
Date of birth                   : {Dob}

    Examination details 

University/College                                             
Exam                            : {Exam1} 
Exam Authority                  : {Auth1} 
Exam Register No                : {Regno1} 
Year of Passing                 : {Yop1}

HigherSecondary                                            
Exam                            : {Exam2} 
Exam Authority                  : {Auth2} 
Exam Register No                : {Regno2} 
Year of Passing                 : {Yop2}

HighSchool                                             
Exam                            : {Exam3} 
Exam Authority                  : {Auth3} 
Exam Register No                : {Regno3} 
Year of Passing                 : {Yop3}

Please sign here               

                        """
            response = HttpResponse(content, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
            return response

        else:
            messages.warning("The following code doesn't exist in this server!")
    elif Export_as_csv!="false":
        print(Export_as_csv)
        details_list = []
        fields = ['Applicants_Name','Branch_Of_Study','Fathers_Name','Address','Email'
        ,'Mobile_Number','Nationality','Roll_Number','College','Year','Batch','Date_Of_Birth']
        # name of csv file 
        filename = "iei_registration_2k21.csv"
        # writing to csv file
        response = HttpResponse(content_type='text/csv')  
        response['Content-Disposition'] = 'attachment; filename="iei_registration_2k21.csv"' 
        writer = csv.writer(response) 
        writer.writerow(fields)  
        for key,value in data_firebase.items():
            writer.writerow(eval(value).values())
        return response   
    return render(request,'WEBSITE/admin-page.html',{"data":data,"count":count})

def test(request):
    if request.method == 'GET':
        form = MyCertGen()
    else:
        form = MyCertGen(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['Username']
                # Create the HttpResponse object
                # packet = io.BytesIO()
            # create a new PDF with Reportlab
            packet = io.BytesIO()
        # create a new PDF with Reportlab
            can = canvas.Canvas(packet, pagesize=letter)
            can.drawString(490, 320, f"{Username}")
            can.save()
            #move to the beginning of the StringIO buffer
            packet.seek(0)
            new_pdf = PdfFileReader(packet)
            # read your existing PDF
            existing_pdf = PdfFileReader(open("WEBSITE/static/pdf/cer.pdf", "rb"))
            output = PdfFileWriter()
            # add the "watermark" (which is the new pdf) on the existing page
            page = existing_pdf.getPage(0)
            page.mergePage(new_pdf.getPage(0))
            output.addPage(page)
            # finally, write "output" to a real file
            outputStream = open(f"WEBSITE/static/pdf/{Username}.pdf", "wb")
            output.write(outputStream)
            outputStream.close()
            return FileResponse(open(f"WEBSITE/static/pdf/{Username}.pdf", 'rb'), content_type='application/pdf')
        else:
           messages.warning(request,"Hey! Make Sure you have given details correctly")
    return render(request,'WEBSITE/test.html',{"form":form})    