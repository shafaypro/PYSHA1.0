import smtplib  # this is the smtp module (simple mail transfer protocol library ! for hte sending and the recieving of the emails !
'''
This is the usage for the Gmail ,
'''

server = smtplib.SMTP('smtp.gmail.com', 587)  # this is the general server for the Smtp client server object! , which creates the object !
# the first one is the server address and the next argument is the port number
server.starttls()  # This starts the communication between the Server and the smtp client


class Email:
    def __init__ (self):
        pass

    def send_email (self, email_id='', email_pw='', message='', email_sendto=''):
        server = smtplib.SMTP('smtp.gmail.com', 587)  # this is the general server for the Smtp client
        server.starttls()  # This starts the communication between the Server and the smtp client
        server.login(email_id, email_pw)  # this is the specification of the email and the password for the email.
        server.sendmail(email_id, email_sendto, message)  # this is the email id , the send email and the message to be send
        server.quit() # this turns of the server
    def recieve_email(self, email_id='', email_pw=''):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Starting the Communication
        server.login(email_id,email_pw) # this logins the server using the email and the passwords.
        server.quit() # Quits the specific server
    def check_email(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)  # This is the General server