import yagmail
def send_mail_dic(subjects,email):
    try:
        #initializing the server connection
        yag = yagmail.SMTP(user='dpservice200@gmail.com', password='Soorajsivadas767')
        #sending the email
        yag.send(to=email, subject=subjects, contents=f'''<h3>
        Hi ,Thank you for showing interest in IEI TKMCE!,
        </h3>
        <br>
        we got your details as follows..
        
        ''')
        print("Email sent successfully")
    except Exception as e:
        print(f"Error, email was not sentn {e}")
send_mail_dic('hi','sjts007@gmail.com')