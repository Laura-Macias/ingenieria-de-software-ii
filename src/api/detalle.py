from flask import Blueprint, render_template

# Definir un Blueprint para la vista detalles
detalle_bp = Blueprint('detalle', __name__)

@detalle_bp.route('/detalle_vacio')
def detalle_vacio():
    return render_template('carrito_vacio.html')

@detalle_bp.route('/detalle_lleno')
def detalle_lleno():
    return render_template('carrito_lleno.html')