// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.getElementById('menuToggle'); // Elemento del botón de menú
    const navLinks = document.getElementById('navLinks'); // Elemento de los enlaces de navegación

    // Función para alternar el menú
    menuToggle.addEventListener('click', function() {
        navLinks.classList.toggle('active'); // Añade o quita la clase 'active' que muestra el menú
    });
});
