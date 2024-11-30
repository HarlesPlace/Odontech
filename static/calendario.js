const daysGrid = document.getElementById("days-grid");
const currentMonth = document.getElementById("current-month");
const agendaModal = document.getElementById("agenda-modal");
const agendaContent = document.querySelector(".agenda-content");
const agendaList = document.getElementById("agenda-list");
const selectedDate = document.getElementById("selected-date");

let currentYear = new Date().getFullYear();
let currentMonthIndex = new Date().getMonth();

const generateCalendar = () => {
    daysGrid.innerHTML = "";
    const date = new Date(currentYear, currentMonthIndex, 1);
    const firstDayIndex = date.getDay();
    const daysInMonth = new Date(currentYear, currentMonthIndex + 1, 0).getDate();

    currentMonth.textContent = date.toLocaleString("default", { month: "long", year: "numeric" });

    // Fill in blank days before first day
    for (let i = 0; i < firstDayIndex; i++) {
        const emptyCell = document.createElement("div");
        daysGrid.appendChild(emptyCell);
    }

    // Fill in days
    for (let i = 1; i <= daysInMonth; i++) {
        const dayCell = document.createElement("div");
        dayCell.textContent = i;
        dayCell.addEventListener("click", () => openAgenda(i));
        daysGrid.appendChild(dayCell);
    }
};

const openAgenda = (day) => {
    selectedDate.textContent = `Dia ${day}`;
    agendaList.innerHTML = "";

    for (let i = 8; i <= 18; i++) {
        const hourItem = document.createElement("li");
        hourItem.textContent = `${i}:00 - ${i + 1}:00`;
        agendaList.appendChild(hourItem);
    }

    agendaModal.style.display = "flex";
};

// Fechar modal ao clicar fora do conteúdo
const closeModalOnOutsideClick = (event) => {
    if (!agendaContent.contains(event.target)) {
        agendaModal.style.display = "none";
    }
};

agendaModal.addEventListener("click", closeModalOnOutsideClick);

document.getElementById("prev-month").addEventListener("click", () => {
    currentMonthIndex = (currentMonthIndex - 1 + 12) % 12;
    generateCalendar();
});

document.getElementById("next-month").addEventListener("click", () => {
    currentMonthIndex = (currentMonthIndex + 1) % 12;
    generateCalendar();
});

generateCalendar();
