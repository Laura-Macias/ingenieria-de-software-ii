const menuToggle = document.getElementById('menuToggle'); // El ícono del menú
const navLinks = document.getElementById('navLinks'); // Lista del menú (usando el ID correcto)
const menuLinks = document.querySelectorAll('nav ul li a'); // Todos los enlaces del menú

// Alternar el menú al hacer clic en el ícono del menú
menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active'); // Muestra u oculta el menú
});

// Cerrar el menú al hacer clic en un enlace del menú
menuLinks.forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active'); // Oculta el menú
    });
});