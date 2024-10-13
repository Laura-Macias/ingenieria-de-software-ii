import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
from flask import request, url_for
import secrets
from itsdangerous import URLSafeTimedSerializer

# Crear un token único con vencimiento

secret_key = secrets.token_hex(16)

def generar_token(email):
    serializer = URLSafeTimedSerializer('SECRET_KEY')
    token = serializer.dumps(email, salt='password-reset-salt')
    return token

# Se cargan las variables de entorno
load_dotenv()

email_sender = 'tsumekireisf2@gmail.com'
password = os.getenv('PASSWORD_EMAIL') # Se trae del archivo .env la variable de entorno que contiene la contraseña

context = ssl.create_default_context() # Se crea un contexto seguro encriptando el email

def send_email_signup(name, email_reciber):
    em = EmailMessage() # Inicializamos el objeto que nos permite usar las funciones de correo
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
    em = EmailMessage() # Inicializamos el objeto que nos permite usar las funciones de correo
    # Enviar correo con el link para restablecer la contraseña
    token = generar_token(email_reciber)
    reset_url = url_for('recover_password.reset_password', token=token, _external=True)  # Genera la URL del link
    subject = 'Recover password'
    body = f'{name}, Para restablecer tu contraseña, haz clic en el siguiente enlace: {reset_url}'
    em["From"] = email_sender
    em["To"] = email_reciber
    em['Subject'] = subject
    em.set_content(body)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_reciber, em.as_string())
