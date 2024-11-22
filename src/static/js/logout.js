function logout() {
    window.location.href = "{{ url_for('auth.logout') }}";
}