from flask import Blueprint, render_template

# Definir un Blueprint para la vista detalles
detalle_bp = Blueprint('detalle', __name__)

@detalle_bp.route('/detalle')
def detalle_vacio():
    return render_template('carrito.html')
