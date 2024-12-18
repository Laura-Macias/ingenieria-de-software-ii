from flask import Blueprint, render_template, request, redirect, url_for, session
from .models.staff import Staff 
from config import Config
from .detalle import obtener_detalle
from flask_login import current_user

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
@reservation_bp.route('/reservation', methods=['GET'])
def reservation():
    detalles = obtener_detalle()
    id_customer = current_user.id_customer
    service_id = request.args.get('service_id') 
    staff = obtener_staff()  # Llama a la función que obtiene el staff

    if staff:  # Verifica si hay manicuristas antes de renderizar
        return render_template('reservation.html', staff=staff, service_id=service_id, current_user=current_user, detalles = detalles)  # Pasa los manicuristas al template
    else:
        return render_template('reservation.html', staff=[], service_id=service_id, current_user=current_user)  # Renderiza con una lista vacía si no hay datos

@reservation_bp.route('/add_reservation_to_detail', methods=['POST'])
def add_reservation_to_detail():
    service_id = request.form.get('service_id')
    esthetician = request.form.get('esthetician')
    time = request.form.get('time')
    id_customer = request.form.get('id_customer')
    selected_date = request.form.get('selected_date')
    
    # Obtener el id_detail desde la sesión (si existe)
    id_detail = session.get('id_detail_to_update')

    # Si id_detail no existe en la sesión, hacer una inserción
    if not id_detail:
        # Inserción de nuevo detalle
         supabase.table('Detail').insert({
            'id_customer': id_customer,
            'id_service': service_id,
            'id_staff': esthetician,
            'time': time,
            'date': selected_date
        }).execute()
    
    else:
        # Si existe id_detail, hacer una actualización
        supabase.table('Detail').update({
            'id_service': service_id,
            'id_staff': esthetician,
            'time': time,
            'date': selected_date
        }).eq('id_detail', id_detail).execute()

    # Limpiar la sesión después de la operación (opcional)
    session.pop('id_detail_to_update', None)

    # Redirigir al usuario al catálogo o a la página que corresponda
    return redirect(url_for('catalog.catalog'))

