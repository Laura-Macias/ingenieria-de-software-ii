// Variables del carrito
let cart = [];
let cartCount = 0;

function addToCart(name, price) {
    console.log("Servicio agregado al carrito:", name, price);  // Verifica si se llama a la función

    // Verifica si el servicio ya está en el carrito
    const existingItem = cart.find(item => item.name === name);
    if (existingItem) {
        alert("Este servicio ya ha sido seleccionado.");
        return;  // Si ya está en el carrito, no agregarlo de nuevo
    }

    // Añadir el nuevo servicio al carrito
    cart.push({ name, price });
    cartCount++;

    // Actualizar el botón del servicio actual a "Seleccionado"
    const button = document.querySelector(`button[data-service-name="${name}"]`);
    if (button) {
        button.textContent = 'Seleccionado';
        button.disabled = true;  // Opcional: Desactivar el botón después de selección
    }

    updateCart();
}

// Función para actualizar el carrito
function updateCart() {
    // Actualizar el contador de carrito
    document.getElementById("cartCount").textContent = cartCount;

    // Actualizar los detalles del carrito
    let cartItems = document.getElementById("cartItems");
    cartItems.innerHTML = '';  // Limpiar los elementos anteriores

    let total = 0;
    cart.forEach(item => {
        let listItem = document.createElement("li");
        // Formatear el precio con separador de miles y símbolo de $
        listItem.textContent = `${item.name} - $${item.price.toLocaleString("es-CO")}`;
        cartItems.appendChild(listItem);
        total += item.price;
    });

    // Actualizar el precio total con formato y símbolo de $
    document.getElementById("totalPrice").textContent = `$${total.toLocaleString("es-CO")}`;

    // Mostrar el botón de Agendar si hay un servicio seleccionado
    document.getElementById("scheduleButton").style.display = cartCount > 0 ? 'inline-block' : 'none';
}

// Función para mostrar/ocultar el carrito
function toggleCart() {
    let cartDetails = document.getElementById("cartDetails");
    cartDetails.style.display = cartDetails.style.display === 'none' ? 'block' : 'none';
}
