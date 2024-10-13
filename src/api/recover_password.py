from flask import render_template, Blueprint, request, redirect, url_for
from config import Config
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
from application.sendEmail import send_recover_password
from werkzeug.security import generate_password_hash

supabase = Config().supabase

recover_password_bp = Blueprint('recover_password', __name__)

@recover_password_bp.route('/recover_password', methods=['GET', 'POST'])
def recover_password():
    if request.method == 'POST':
        email = request.form['email']

        # Consulta a Supabase para verificar el usuario
        response = supabase.table('Customer').select("*").eq('email', email).execute()
 
        if response.data:  # Si la respuesta tiene datos
            user_data = response.data[0]  # Obtenemos el primer usuario devuelto
            print(user_data['name'])
            # Enviamos un correo con los pasos para la recuperacion de la contarseña
            send_recover_password(user_data['name'], user_data['email'])

        return redirect(url_for('auth.login'))  # Redirige de nuevo al login después de enviar el correo
    return render_template('recover_password.html')

# Define una ruta para la URL '/reset_password/<token>'
# La variable <token> en la URL será pasada a la función 'reset_password'.
@recover_password_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    
    # Crea un serializador que permite generar y validar tokens usando una clave secreta.
    serializer = URLSafeTimedSerializer('SECRET_KEY')
    
    try:
        # Intenta decodificar el token recibido en la URL y obtener el email asociado.
        # El token se valida con una sal específica ('password-reset-salt') y expira después de 30 minutos (1800 segundos).
        email = serializer.loads(token, salt='password-reset-salt', max_age=1800)
    except (SignatureExpired, BadTimeSignature):
        # Si el token ha expirado o es inválido, se retorna un error.
        return "El token ha expirado o es inválido", 400

    if request.method == 'POST':
        # Obtiene la nueva contraseña y su confirmación desde el formulario.
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # Verifica que ambas contraseñas coincidan.
        if new_password == confirm_password:

            # Si coinciden, genera el hash de la nueva contraseña.
            hashed_password = generate_password_hash(new_password)

            # Actualiza la contraseña del usuario en la tabla 'cliente' de la base de datos Supabase, utilizando su email.
            response = supabase.table('Customer').update({"password": hashed_password}).eq("email", email).execute()

            # Verifica si la actualización fue exitosa.
            if response.data:  
                # Si hay datos en la respuesta, significa que la actualización fue exitosa.
                # Redirige al usuario a la página de login después de actualizar la contraseña.
                return redirect(url_for('auth.login'))
            else:
                # Si la actualización falla, redirige de nuevo a la página de restablecimiento de contraseña con el token.
                return redirect(url_for('recover_password.reset_password', token=token))
        else:
            # Si las contraseñas no coinciden, redirige de nuevo a la página de restablecimiento de contraseña.
            return redirect(url_for('recover_password.reset_password', token=token))

    return render_template('reset_password.html', token=token)