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

    function renderCalendar() {
        daysContainer.innerHTML = "";
        monthElement.textContent = `${months[currentMonth]} ${currentYear}`;

        const firstDay = new Date(currentYear, currentMonth, 1).getDay();
        const lastDay = new Date(currentYear, currentMonth + 1, 0).getDate();

        for (let i = 0; i < firstDay; i++) {
            const emptyDay = document.createElement("div");
            emptyDay.classList.add("day", "empty");
            daysContainer.appendChild(emptyDay);
        }

        for (let day = 1; day <= lastDay; day++) {
            const dayElement = document.createElement("div");
            dayElement.classList.add("day");
            dayElement.textContent = day;

            if (
                day === date.getDate() &&
                currentMonth === date.getMonth() &&
                currentYear === date.getFullYear()
            ) {
                dayElement.classList.add("today");
            }

            dayElement.addEventListener("click", () => {
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
});
