from flask import Blueprint, render_template
from .models.detail import Detail
from config import Config

# Definir un Blueprint para la vista detalles
detalle_bp = Blueprint('detalle', __name__, url_prefix='/detalle')
supabase = Config.supabase


def detalle():
        
    try:
        response = supabase.table('Detail').select('id_detail, id_customer, id_service, id_staff, date, Catalog(id_catalog, service_name, price)').execute()
        if not response.data:
            print("No se encontraron detalles en la base de datos.")
            
            return []
        return [Detail(**item) for item in response.data]
    except Exception as e:
        print(f"Error al obtener el detalle: {e}")
        return []


#return render_template('carrito.html')

@detalle_bp.route('/')
def detalle_vacio():
    servicios = detalle()  # Llama a la función que obtiene el detalles
    if servicios:  # Verifica si hay productos antes de renderizar
        return render_template('carrito.html', servicios=servicios)  # Pasa los productos al template
    else:
        return render_template('carrito.html', servicios=[])  # Renderiza con una lista vacía si no hay productos

