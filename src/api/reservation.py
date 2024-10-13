from flask import render_template, Blueprint


reservation_bp = Blueprint('reservation', __name__)

@reservation_bp.route('/reservation')
def reservation():
    return render_template('reservation.html')