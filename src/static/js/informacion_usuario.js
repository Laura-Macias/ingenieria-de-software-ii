// Alternar la visibilidad del menú
function toggleProfileMenu() {
    const menu = document.getElementById('profileMenu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}

// Redirigir a la vista de edición
function editProfile() {
    window.location.href = "{{ url_for('profile.edit') }}";
}

// Manejar el cierre de sesión
function logout() {
    // Muestra el mensaje de carga
    alert('Cerrando sesión...');
    // Redirige a la vista de cierre de sesión
    window.location.href = "{{ url_for('auth.logout') }}";
}

function toggleEditMode() {
    // Mostrar/ocultar los campos de edición
    const userDetails = document.getElementById('userDetails');
    const userDetailsEdit = document.getElementById('userDetailsEdit');
    const editButton = document.getElementById('editButton');
    const saveButton = document.getElementById('saveButton');
    
    userDetails.style.display = userDetails.style.display === 'none' ? 'block' : 'none';
    userDetailsEdit.style.display = userDetailsEdit.style.display === 'none' ? 'block' : 'none';
    
    // Cambiar el texto del botón
    if (editButton.style.display === 'none') {
        editButton.style.display = 'block';
        saveButton.style.display = 'none';
    } else {
        editButton.style.display = 'none';
        saveButton.style.display = 'block';
    }
}

// Mostrar el popup de cierre de sesión
function logout() {
    // Muestra el popup de cierre de sesión
    const logoutPopup = document.getElementById('logoutPopup');
    logoutPopup.style.display = 'flex'; // Muestra el popup
}

// Confirmar el cierre de sesión
function confirmLogout() {
    // Redirige a la página de cierre de sesión
    window.location.href = "{{ url_for('auth.logout') }}";
}

// Cancelar el cierre de sesión
function cancelLogout() {
    // Oculta el popup
    const logoutPopup = document.getElementById('logoutPopup');
    logoutPopup.style.display = 'none';
}