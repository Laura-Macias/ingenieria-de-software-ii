from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import current_user
from .models.detail import Detail
from .models.catalog import Catalogo
from config import Config

# Definir un Blueprint para la vista detalles
detalle_bp = Blueprint('detalle', __name__, url_prefix='/detalle')
supabase = Config.supabase

@detalle_bp.route('/delete', methods=['POST'])
def eliminar_detalle():
    if request.method == 'POST':
        
        id_detail = request.form['id_detail']
        
        response = supabase.table('Detail').delete().eq('id_detail', id_detail).execute()
        return redirect(url_for('detalle.detalle_vacio'))  
    
    return redirect(url_for('detalle.detalle_vacio'))

def obtener_detalle():
        
    try:
        response = supabase.table('Detail').select('*').eq('id_customer', current_user.id_customer).execute()

        if not response.data:
            print("No se encontraron detalles en la base de datos.")
            
            return []
        return [Detail(**item) for item in response.data]
    except Exception as e:
        print(f"Error al obtener el detalle: {e}")
        return []

@detalle_bp.route('/actualizar', methods=['GET', 'POST'])
def actualizar_detalle():
    id_detail = request.args.get('id_detail') 
    detalles = obtener_detalle()
    print ("Id detalle:", id_detail)
    if request.method == 'POST':
        try:
            id_detail = session.get('id_detail_to_update')
            service_id = request.form.get('service_id')  
            esthetician = request.form.get('esthetician')
            time = request.form.get('time')
            id_customer = request.form.get('id_customer')
            selected_date = request.form.get('selected_date')

            print("Datos recibidos:", service_id, esthetician, time, id_customer, selected_date)
            
            supabase.table('Detail').update({
                    'id_detail': id_detail,
                    'id_customer': id_customer,
                    'id_service': service_id,
                    'id_staff': esthetician,
                    'time': time,
                    'date': selected_date
                }).execute()
            
            return redirect(url_for('catalog.catalog'))
        except Exception as e:
            print(f"Error al actualizar el detalle: {e}")

    for detalle in detalles:
        if detalle.id_detail == id_detail:
            service_id = id_detail
    return redirect(url_for('calendar.calendar', service_id = id_detail))
  
    
def catalogo():
        
    try:
        response = supabase.table('Catalog').select('*').execute()
        
        if not response.data:
            print("No se encontraron detalles en la base de datos.")
            
            return []
        return [Catalogo(**item) for item in response.data]
    except Exception as e:
        print(f"Error al obtener el detalle: {e}")
        return []

#return render_template('carrito.html')

@detalle_bp.route('/')
def detalle_vacio():
    servicios = obtener_detalle()  # Llama a la función que obtiene el detalles
    items = catalogo()
    print (servicios)
    if servicios:  # Verifica si hay productos antes de renderizar
        return render_template('carrito.html', servicios=servicios, items = items)  # Pasa los productos al template
    else:
        return render_template('carrito.html', servicios=[])  # Renderiza con una lista vacía si no hay productos

