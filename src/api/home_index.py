from flask import Blueprint, render_template
from flask_login import login_required
from .models.staff import Staff
from config import Config

# Definir un Blueprint para la vista principal segun el usuario entra a la app por primera vez
home_index_bp = Blueprint('home_index', __name__)
supabase = Config.supabase
def staff():
        
    try:
        response = supabase.table('Staff').select('*').execute()
        
        if not response.data:
            print("No se encontraron detalles en la base de datos.")
            
            return []
        return [Staff(**item) for item in response.data]
    except Exception as e:
        print(f"Error al obtener el detalle: {e}")
        return []
    
@home_index_bp.route('/home_index')
def home_index():
    employees = staff()
    print (employees)
    return render_template('home_index.html', employees = employees)