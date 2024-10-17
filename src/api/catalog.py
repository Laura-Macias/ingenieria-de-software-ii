from flask import Blueprint, render_template

# Definir un Blueprint para la vista principal segun el usuario entra a la app por primera vez
catalog_bp = Blueprint('catalog', __name__, url_prefix='/catalog')  # Añade un prefijo
@catalog_bp.route('/')
def catalog():
    return render_template('catalog.html')