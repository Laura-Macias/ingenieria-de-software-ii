from flask import Blueprint, render_template, request

# Definir un Blueprint para la vista principal segun el usuario entra a la app por primera vez
pay_bp = Blueprint('pay', __name__)

@pay_bp.route('/pay', methods=['GET', 'POST'])
def pay():
    if request.method == 'POST':
        return render_template('pay.html')
    return render_template('pay.html')