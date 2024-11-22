from flask import Blueprint, render_template
from flask_login import current_user, login_required
from config import Config

consulta_bp = Blueprint('consulta', __name__, url_prefix='/consulta')
supabase = Config.supabase

def obtener_consulta():
    """
    Obtiene la información de los turnos agendados por el cliente actual desde la tabla 'calendar',
    incluyendo el manicurista, la descripción del servicio y el id del cliente.
    """
    try:
        print(f"ID del cliente logueado: {current_user.id_customer}")
        
        # Consultamos los turnos para el cliente actual
        turnos = supabase.table('Calendar').select('event_date, id_customer_calendar, id_catalog_calendar, id_staff_calendar') \
            .eq('id_customer_calendar', current_user.id_customer).execute()

        if not turnos.data:
            print("No se encontraron turnos agendados en la base de datos.")
            return []

        # Obtenemos los nombres de los manicuristas y la descripción de los servicios
        for turno in turnos.data:
            id_staff_calendar = turno['id_staff_calendar']
            id_catalog_calendar = turno['id_catalog_calendar']

            # Consultamos el nombre completo del manicurista
            manicurista = supabase.table('Staff').select('name_staff, last_name_staff').eq('id_staff', id_staff_calendar).execute()

            if manicurista.data:
                turno['manicurist_name'] = f"{manicurista.data[0]['name_staff']} {manicurista.data[0]['last_name_staff']}"
            else:
                turno['manicurist_name'] = "No disponible"

            # Consultamos la información del servicio
            servicio = supabase.table('Catalog').select('service_name, description').eq('id_catalog', id_catalog_calendar).execute()

            if servicio.data:
                turno['service_name'] = servicio.data[0]['service_name']
                turno['description'] = servicio.data[0]['description']
            else:
                turno['service_name'] = "No disponible"
                turno['description'] = "Descripción no disponible"

        # Retornamos los turnos con toda la información
        return turnos.data

    except Exception as e:
        print(f"Error al obtener la información de los turnos: {e}")
        return []



@consulta_bp.route('/')
@login_required
def consulta_view():
    """
    Renderiza la vista con la información de los turnos agendados por el cliente actual.
    """
    turnos = obtener_consulta()
    print(turnos)

    # Verificación para depurar los turnos obtenidos
    if turnos:
        print(f"Turnos obtenidos: {turnos}")
    else:
        print("No se obtuvieron turnos")

    return render_template('consulta.html', turnos=turnos)

def catalog_view():
    return render_template('catalog.html')
