from flask import Blueprint, render_template

# Definir un Blueprint para la vista principal segun el usuario entra a la app por primera vez
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')