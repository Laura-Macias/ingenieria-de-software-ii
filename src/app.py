from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from supabase import create_client
from datetime import date
from application.sendEmail import send_email_signup, send_recover_password

from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature

# Configurar Supabase
url = "https://usgedyofxwmrdrwjkwhq.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVzZ2VkeW9meHdtcmRyd2prd2hxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjcwNjE4NzcsImV4cCI6MjA0MjYzNzg3N30.EA8Y-9VFPqCGAobgfE4Iu2NsNVv9OlR1OiQcGMZMyVI"
supabase = create_client(url, key)

app = Flask(__name__)
app.secret_key = '123456'

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirecciona a la vista de login si no está autenticado


# Modelo de usuario para Flask-Login
class User(UserMixin):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

# Carga el usuario para Flask-Login
@login_manager.user_loader
def load_user(user_id):
    response = supabase.table('cliente').select('*').eq('id_cliente', user_id).execute()
    if response.data:
        user_data = response.data[0]
        return User(user_data['id_cliente'], user_data['name'], user_data['email'])
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Consulta a Supabase para verificar el usuario
        response = supabase.table('cliente').select("*").eq('email', email).execute()
        
        print(response)
 
        if response.data:  # Si la respuesta tiene datos
            user_data = response.data[0]  # Obtenemos el primer usuario devuelto
            
            if check_password_hash(user_data['password'], password):
                # Autenticar el usuario
                user = User(user_data['id_cliente'], user_data['name'], user_data['email'])
                login_user(user)
                flash("Inicio de sesión exitoso.")
                
                return redirect(url_for('home'))
            else:
                flash('Contraseña incorrecta.', 'error')
                return redirect(url_for('login'))
        else:
            flash('Usuario no encontrado.', 'error')
            return redirect(url_for('login'))
        
        
    
    return render_template('login.html')

# Ya podemos usar la informacion del cliente logueado en la logica
print(login_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada correctamente.")
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name)

@app.route('/recover_password', methods=['GET', 'POST'])
def recover_password():
    if request.method == 'POST':
        
        email = request.form['email']

        # Consulta a Supabase para verificar el usuario
        response = supabase.table('cliente').select("*").eq('email', email).execute()
 
        if response.data:  # Si la respuesta tiene datos
            user_data = response.data[0]  # Obtenemos el primer usuario devuelto
            print(user_data['name'])
            send_recover_password(user_data['name'], user_data['email'])

        # Lógica para enviar el correo electrónico de recuperación
        return redirect(url_for('login'))  # Redirige de nuevo al login después de enviar el correo
    return render_template('recover_password.html')  # Crea una plantilla para esto

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    serializer = URLSafeTimedSerializer('SECRET_KEY')
    
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=1800)  # 30 minutos de validez
    except (SignatureExpired, BadTimeSignature):
        return "El token ha expirado o es inválido", 400

    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password == confirm_password:
            hashed_password = generate_password_hash(new_password)
            response = supabase.table('cliente').update({"password": hashed_password}).eq("email", email).execute()

            # Verifica si la actualización fue exitosa
            if response.data:  # Si hay datos, significa que la actualización fue exitosa
    
                return redirect(url_for('login'))
            else:
             
                return redirect(url_for('reset_password', token=token))
        else:
     
            return redirect(url_for('reset_password', token=token))

    return render_template('reset_password.html', token=token)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']

        # Verifica si el correo ya existe
        response = supabase.table('cliente').select('email').eq('email', email).execute()

        if response.data and len(response.data) > 0:
            flash("El correo electrónico ya está en uso. Por favor, ingrese otro.")
            return render_template('signup.html')

        hashed_password = generate_password_hash(password)

        # Inserta los datos en la base de datos
        response = supabase.table('cliente').insert({
            'name': name.upper(),
            'last_name' : last_name.upper(),
            'phone': phone,
            'email': email,
            'date': date.today().isoformat(),
            'password': hashed_password
        }).execute()

        if response.data:
            send_email_signup(name, email)         
        else:
            flash("Error al registrar: " + str(response.error))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)