function openMenu() {
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("overlay");
    
    // Adiciona a classe "open" ao menu e exibe o overlay
    sidebar.classList.add("open");
    overlay.style.display = "block";
}

function closeMenu() {
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("overlay");
    
    // Remove a classe "open" do menu e oculta o overlay
    sidebar.classList.remove("open");
    overlay.style.display = "none";
}