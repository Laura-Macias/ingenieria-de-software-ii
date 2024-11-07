from flask import Blueprint, render_template, jsonify
from .models.catalog import Catalogo  
from config import Config

# Se define el Blueprint para las rutas del catálogo
catalog_bp = Blueprint('catalog', __name__, url_prefix='/catalog')
supabase = Config.supabase

# Función para obtener el catálogo
def obtener_catalogo():
    
    try:
        response = supabase.table('Catalog').select('*').execute()
        
        if not response.data:
            print("No se encontraron productos en la base de datos.")
            return []
        return [Catalogo(**item) for item in response.data]
    except Exception as e:
        print(f"Error al obtener el catálogo: {e}")
        return []
    
def verificar_disponibilidad(servicio_id):
    
    try:
        # Ejemplo de consulta de disponibilidad en la base de datos
        response = supabase.table('Catalog').select('*').eq('id_catalog', servicio_id).execute()
        return bool(response.data)  # Retorna True si el servicio está disponible
    except Exception as e:
        print(f"Error al verificar disponibilidad: {e}")
        return False  # Retorna False en caso de error

# Ruta para renderizar la vista del catálogo con plantilla HTML
@catalog_bp.route('/')
def catalog():
    servicios = obtener_catalogo()  # Llama a la función que obtiene el catálogo
    if servicios:  # Verifica si hay productos antes de renderizar
        return render_template('catalog.html', servicios=servicios)  # Pasa los productos al template
    else:
        return render_template('catalog.html', servicios=[])  # Renderiza con una lista vacía si no hay productos


# Ruta para obtener los productos del catálogo en formato JSON
@catalog_bp.route('/api', methods=['GET'])
def obtener_catalogo_api():
    productos = obtener_catalogo()  # Obtiene los productos del catálogo
    return jsonify([producto.serialize() for producto in productos]), 200  # Serializa y devuelve en JSON
