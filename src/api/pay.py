from flask import Blueprint, render_template, request
from flask_login import current_user
from .models.detail import Detail
from .models.catalog import Catalogo
from .models.transaction import Transaction
from application.sendEmail import finished_transaction
from config import Config
from datetime import date

# Definir un Blueprint para la vista principal segun el usuario entra a la app por primera vez
pay_bp = Blueprint('pay', __name__, url_prefix='/pay')

supabase = Config.supabase

def traer_transacciones():
    try:
        # Realizamos la consulta para traer las transacciones del cliente
        response = supabase.table('Transaction').select('*').execute()
        
        if not response.data:
            print("No se encontraron detalles en la base de datos.")
            
            return []
        return [Transaction(**item) for item in response.data]
    except Exception as e:
        print(f"Error al obtener el detalle: {e}")
        return []


def traer_detalles():
        
    try:
        response = supabase.table('Detail').select('*').eq('id_customer', current_user.id_customer).execute()
        
        if not response.data:
            print("No se encontraron detalles en la base de datos.")
            
            return []
        return [Detail(**item) for item in response.data]
    except Exception as e:
        print(f"Error al obtener el detalle: {e}")
        return []

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

def amount():
    detalles = traer_detalles()
    items = catalogo()
    amount = 0
    for detalle in detalles:
        for item in items:
            if detalle.id_service == item.id_catalog:
                amount += item.price
    return amount

def agregar_calendario():
    servicios = traer_detalles()
    transacciones = traer_transacciones()
    for servicio in servicios:
        for transaccion in transacciones:
            # Asegurarnos de que el servicio pertenece a la transacción correcta
            if servicio.id_customer == transaccion.id_customer_transaction:
                # Insertar en la tabla Calendar
                response = supabase.table('Calendar').insert({
                    'event_date': servicio.date,
                    'id_customer_calendar': servicio.id_customer,
                    'id_catalog_calendar': servicio.id_service,  
                    'id_staff_calendar': servicio.id_staff,
                    'id_transaccion': transaccion.id_transaction[0]
                }).execute()


@pay_bp.route('/', methods=['GET', 'POST'])
def pay():
    servicios = traer_detalles()
    items = catalogo()
    total = amount()
    if request.method == 'POST':
        payment_method = request.form['payment']
        account_number = request.form['card_number']
        
        response = supabase.table('Transaction').insert({
            'account_number': account_number,
            'total': total,
            'transaction_date': date.today().isoformat(),
            'payment_method': payment_method,
            'id_customer_transaction': current_user.id_customer,
        }).execute()

        if response.data:
            finished_transaction(current_user.name, total, servicios, items, current_user.email) 

            agregar_calendario()

            for servicios in servicios:
                supabase.table('Detail').delete().eq('id_customer', current_user.id_customer).execute()

        return render_template('home_index.html')
    return render_template('pay.html')