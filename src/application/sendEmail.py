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

def finished_transaction(name, total, services, items, email_reciber):
    em = EmailMessage()  # Inicializamos el objeto que nos permite usar las funciones de correo

    # Crear la lista de servicios en formato de texto
    services_list = []
    for service in services:
        # Buscar el servicio en 'items' que coincida con el 'id_catalog' de 'service'
        for item in items:
            if service.id_service == item.id_catalog:  # Compara el id_service con el id_catalog
                services_list.append(f"{item.service_name} - ${item.price}")

    # Convertir la lista de servicios a una cadena de texto con saltos de línea
    services_list_text = "\n".join(services_list)

    # Crear el cuerpo del correo con el resumen
    body = f'{name}, Este es el resumen de tu compra: \n\n'
    body += f"Servicios comprados:\n{services_list_text}\n"
    body += f"\nTotal: ${total}"

    em["From"] = email_sender
    em["To"] = email_reciber
    em['Subject'] = 'Purchase in Tsume Kirei'
    em.set_content(body)

    # Enviar el correo
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_reciber, em.as_string())


