from flask import Blueprint, render_template
from .models.staff import Staff 
from config import Config

# Se define el Blueprint para las rutas del catálogo
reservation_bp = Blueprint('reservation', __name__)
supabase = Config.supabase

# Función para obtener el catálogo
def obtener_staff():
    
    try:
        response = supabase.table('Staff').select('*').execute()
        #print(response)
        if not response.data:
            print("No se encontraron los manicuristas en la base de datos.")
            return []
        return [Staff(**item) for item in response.data]
    except Exception as e:
        print(f"Error al obtener los datos: {e}")
        return []

# Ruta para renderizar la vista del catálogo con plantilla HTML
@reservation_bp.route('/reservation')
def reservation():
    staff = obtener_staff()  # Llama a la función que obtiene el staff

    if staff:  # Verifica si hay manicuristas antes de renderizar
        return render_template('reservation.html', staff=staff)  # Pasa los manicuristas al template
    else:
        return render_template('reservation.html', staff=[])  # Renderiza con una lista vacía si no hay datos
