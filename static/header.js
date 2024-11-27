// Abrir o menu lateral
function openMenu() {
    document.getElementById("sidebar").style.width = "250px"; // Largura do menu
    document.getElementById("overlay").style.display = "block"; // Mostrar o overlay
}

// Fechar o menu lateral
function closeMenu() {
    document.getElementById("sidebar").style.width = "0"; // Esconder o menu
    document.getElementById("overlay").style.display = "none"; // Esconder o overlay
}
