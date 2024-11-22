from flask import Blueprint, render_template

# Definir un Blueprint para la vista principal segun el usuario entra a la app por primera vez
user_bp = Blueprint('user', __name__)

@user_bp.route('/user')
def user():
    return render_template('user.html')