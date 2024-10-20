from flask import Blueprint, render_template
from flask_login import login_required

# Definir un Blueprint para la vista principal segun el usuario entra a la app por primera vez
home_index_bp = Blueprint('home_index', __name__)

@home_index_bp.route('/home_index')
def home_index():
    return render_template('home_index.html')