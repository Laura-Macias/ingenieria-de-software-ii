import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

# Se cargan las variables de entorno
load_dotenv()

email_sender = 'tsumekireisf2@gmail.com'
password = os.getenv('PASSWORD_EMAIL') # Se trae del archivo .env la variable de entorno que contiene la contraseña

em = EmailMessage() # Inicializamos el objeto que nos permite usar las funciones de correo


context = ssl.create_default_context() # Se crea un contexto seguro encriptando el email

def send_email_signup(name, email_reciber):
    subject = 'Successful Sign up'
    body = f'{name}, tu regsitro en la pagina web de Tsume Kirei ha sido exitoso.'
    em["From"] = email_sender
    em["To"] = email_reciber
    em['Subject'] = subject
    em.set_content(body)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_reciber, em.as_string())

def send_recover_password(name, email_reciber):
    subject = 'Recover password'
    body = f'{name}, usa el siguiente ling para recuperar contraseña. http://127.0.0.1:5000/recover_password'
    em["From"] = email_sender
    em["To"] = email_reciber
    em['Subject'] = subject
    em.set_content(body)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_reciber, em.as_string())
