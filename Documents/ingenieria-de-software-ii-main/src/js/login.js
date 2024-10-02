document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();  // Evita el envío normal del formulario
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Envía una solicitud POST a Flask con los datos del formulario
    const response = await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });

    const result = await response.json();
    if (result.success) {
        alert('Login exitoso');
        // Redirige o maneja el login exitoso
    } else {
        alert('Error en el login');
    }
});