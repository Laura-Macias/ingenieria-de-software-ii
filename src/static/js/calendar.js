document.addEventListener("DOMContentLoaded", () => { 
    const monthElement = document.querySelector(".month");
    const daysContainer = document.querySelector(".days");
    const prevButton = document.querySelector(".prev-btn");
    const nextButton = document.querySelector(".next-btn");
    const todayButton = document.querySelector(".today-btn");

    const months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];
    let date = new Date();
    let currentMonth = date.getMonth();
    let currentYear = date.getFullYear();

    // Función para renderizar el calendario
    function renderCalendar() {
        daysContainer.innerHTML = "";
        monthElement.textContent = `${months[currentMonth]} ${currentYear}`;

        const firstDay = new Date(currentYear, currentMonth, 1).getDay();
        const lastDay = new Date(currentYear, currentMonth + 1, 0).getDate();

        // Renderizar los días vacíos antes del primer día del mes
        for (let i = 0; i < firstDay; i++) {
            const emptyDay = document.createElement("div");
            emptyDay.classList.add("day", "empty");
            daysContainer.appendChild(emptyDay);
        }

        // Renderizar los días del mes
        for (let day = 1; day <= lastDay; day++) {
            const dayElement = document.createElement("div");
            dayElement.classList.add("day");
            dayElement.textContent = day;

            // Marcar el día actual
            if (day === date.getDate() && currentMonth === date.getMonth() && currentYear === date.getFullYear()) {
                dayElement.classList.add("today");
            }

            // Al hacer click en un día, mostrar el iframe
            dayElement.addEventListener("click", () => {
                document.getElementById('form-container').style.display = 'block'; 
            });

            daysContainer.appendChild(dayElement);
        }
    }

    // Manejadores de eventos para los botones de navegación
    prevButton.addEventListener("click", () => {
        currentMonth--;
        if (currentMonth < 0) {
            currentMonth = 11;
            currentYear--;
        }
        renderCalendar();
    });

    nextButton.addEventListener("click", () => {
        currentMonth++;
        if (currentMonth > 11) {
            currentMonth = 0;
            currentYear++;
        }
        renderCalendar();
    });

    todayButton.addEventListener("click", () => {
        date = new Date();
        currentMonth = date.getMonth();
        currentYear = date.getFullYear();
        renderCalendar();
    });

    renderCalendar();

    // Escuchar mensajes del iframe
    window.addEventListener("message", function(event) {
        // Verificar que el mensaje provenga del iframe
        if (event.origin !== window.location.origin) {
            return;  // Ignorar mensajes de orígenes no confiables
        }

        // Verificar si el mensaje es "formSubmitted"
        if (event.data === "formSubmitted") {
            // Ocultar el iframe
            document.getElementById("form-container").style.display = "none";

            // Redirigir a otra página (en este caso la URL de pago)
            window.location.href = "{{ url_for('pay.pay') }}"; // Aquí usas el URL de pago o el que desees
        }
    });
});
