from flask import render_template, Blueprint, request, flash
from config import Config
from werkzeug.security import generate_password_hash
from application.sendEmail import send_email_signup
from datetime import date

supabase = Config().supabase

# Definir un Blueprint para las rutas de la logica de registro 
signup_bp = Blueprint('signup', __name__)

# Esta funcion captura los datos del ususario del formulario del signup desde el Front End
@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    
    if request.method == 'POST':
        '''
        Si se envian los datos del usuarios se capturan con el objeto request importado de Flask
        y se guardan cada uno en una varible
        '''
        name = request.form['name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']

        # Verifica si el correo ya existe
        response = supabase.table('Customer').select('email_customer').eq('email_customer', email).execute()

        # Si  el correo ya existe se envia una alerta al usuairo y se vuelve a cargar la vista del signup
        if response.data and len(response.data) > 0:
            flash("El correo electrónico ya está en uso. Por favor, ingrese otro.")
            return render_template('signup.html')

        # Se cifra la contraseña para no guardarla en texto plano
        hashed_password = generate_password_hash(password)

        # Inserta los datos en la base de datos
        response = supabase.table('Customer').insert({
            'name_customer': name.upper(),
            'last_name_customer': last_name.upper(),
            'phone_customer': phone,
            'email_customer': email,
            'registration_date_customer': date.today().isoformat(),
            'password_customer': hashed_password
        }).execute()

        # Si la variable tiene datos se confirma que se gaurdo en la base de datos y se envia un correo de confrimacion
        if response.data:
            send_email_signup(name, email)         
        else:
            flash("Error al registrar: " + str(response.error))

    return render_template('signup.html')