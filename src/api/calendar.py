from flask import render_template, Blueprint, request


calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/calendar')
def calendar():
    service_id = request.args.get('service_id')  # Captura el ID del servicio
    return render_template('calendar.html')