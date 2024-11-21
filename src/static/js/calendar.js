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
    let selectedDay = null;

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

        for(let day = 1 ; day <= lastDay ; day ++){

            const dayElement = document.createElement("div");
            dayElement.classList.add('day');
            dayElement.textContent = day ;

            if (day === date.getDate() && currentMonth === date.getMonth() && currentYear === date.getFullYear()) {
                dayElement.classList.add("today");
            }

            dayElement.addEventListener("click", () => {
                
                    if(selectedDay){
                        selectedDay.classList.remove("selected");
                    }

                    selectedDay = dayElement;
                    dayElement.classList.add('selected')
                    document.getElementById('form-container').style.display = 'block'; 
            });

            daysContainer.appendChild(dayElement);
        }
    }

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

    window.addEventListener("message", function(event) {
        if (event.origin !== window.location.origin) {
            return;
        }

        if (event.data === "formSubmitted") {
            document.getElementById("form-container").style.display = "none";

            window.location.href = "/catalog";
        }
    });
});
