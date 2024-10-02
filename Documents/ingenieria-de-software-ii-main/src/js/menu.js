const menuToggle = document.getElementById('menuToggle');
    const nav = document.querySelector('nav ul');
    const menuLinks = document.querySelectorAll('nav ul li a'); // Selecciona todos los enlaces del menú

    // Alternar el menú al hacer clic en el ícono del menú
    menuToggle.addEventListener('click', () => {
        nav.classList.toggle('active');
    });

    // Cerrar el menú al hacer clic en un enlace del menú
    menuLinks.forEach(link => {
        link.addEventListener('click', () => {
            nav.classList.remove('active');  // Oculta el menú
        });
    });