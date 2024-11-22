const signupForm = document.getElementById('signupForm');

signupForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Puntos de depuración
    console.log('Datos del formulario:', name, phone, email, password); // Verifica los datos en la consola del navegador

    try {
        const response = await fetch('http://localhost:5000/signup', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, phone, email, password })
        });

        const result = await response.json();
        console.log('Respuesta del servidor:', result); // Verifica la respuesta del servidor en la consola del navegador

        if (response.ok) {
            alert('Registro exitoso!');
            setTimeout(function() {
                window.location.href = "{{ url_for('auth.login') }}"; // Redirige a la página de login después de 3 segundos
            }, 10000);
        } else {
            alert('Error en el registro:', result.message);
        }
    } catch (error) {
        console.error('Error en la solicitud:', error);
    }
});