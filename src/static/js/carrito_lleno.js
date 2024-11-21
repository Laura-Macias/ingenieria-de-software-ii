        // llenado para mostrar la simulación del carrito lleno (esto se borra)
        const carritoLleno = document.querySelector('.carrito-lleno');
        
        // Cambia este valor para probar las diferentes fases
        const hayProductos = true; //Aqui este true es para cambiar de vistas, dejarlo en true

        if (hayProductos) {
            carritoVacio.style.display = 'none';
            carritoLleno.style.display = 'block';
        } else {
            carritoVacio.style.display = 'block';
            carritoLleno.style.display = 'none';
        }