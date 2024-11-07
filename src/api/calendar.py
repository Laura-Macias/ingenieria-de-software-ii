from flask import render_template, Blueprint


calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/calendar')
def calendar():
    return render_template('calendar.html')