// llenado para mostrar la simulación del carrito vacio (esto se borra)
const carritoVacio = document.querySelector('.carrito-vacio');
        
// Cambia este valor para probar las diferentes fases
const hayProductos = false; //Aqui este true es para cambiar de vistas, dejarlo en false

if (hayProductos) {
    carritoVacio.style.display = 'none';
    carritoLleno.style.display = 'block';
} else {
    carritoVacio.style.display = 'block';
    carritoLleno.style.display = 'none';
}