from flask import Flask
from flask_login import LoginManager
from .models.user import User  # Importar la clase User
from .auth import auth_bp
from .home  import home_bp
from .signup import signup_bp
from .recover_password import recover_password_bp
from .reservation import reservation_bp
from .home_index import home_index_bp
from .catalog import catalog_bp
from .calendar import calendar_bp
from .pay import pay_bp
from config import Config

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    app.secret_key = Config().SECRET_KEY

    supabase = Config().supabase

    # Configuración de Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Redirecciona a la vista de login si no está autenticado

    # Carga el usuario para Flask-Login y guarda los datos en la clase User para su posterior uso
    @login_manager.user_loader
    def load_user(user_id):
        response = supabase.table('Customer').select('*').eq('id_customer', user_id).execute()
        if response.data:
            user_data = response.data[0]
            return User(user_data['id_customer'], user_data['name'], user_data['last_name'], user_data['address'], user_data['phone'], user_data['email'])
        return None

    # Registrar los bluprints de cada logica de la aplicacion
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(signup_bp)
    app.register_blueprint(recover_password_bp)
    app.register_blueprint(reservation_bp)
    app.register_blueprint(home_index_bp)
    app.register_blueprint(catalog_bp)
    app.register_blueprint(calendar_bp)
    app.register_blueprint(pay_bp)

    return app