from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from .models.customer import Customer
from config import Config
from werkzeug.security import check_password_hash

supabase = Config().supabase

# Definir un Blueprint para las rutas gde autentucacion
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Consulta a Supabase para verificar el usuario
        response = supabase.table('Customer').select("*").eq('email', email).execute()
 
        if response.data:  # Si la respuesta tiene datos
            user_data = response.data[0]  # Obtenemos el primer usuario devuelto
            
            if check_password_hash(user_data['password'], password):
                # Autenticar el usuario
                user = Customer(user_data['id_customer'], user_data['name'], user_data['last_name'], user_data['address'], user_data['phone'], user_data['email'])
                # se guarda la informacion del usuario en login_user para que se pueda usar en otros procesos
                login_user(user)
                
                return redirect(url_for('home_index.home_index', current_user=current_user))
            else:
                return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('auth.login'))
        
    return render_template('login.html')

# Funcion que permite cerrar cesion
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada correctamente.")
    return redirect(url_for('auth.login'))

