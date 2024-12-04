// Function to open the side menu
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    localStorage.setItem("menuState", "open");
}

// Function to close the side menu
function closeNav() {
    document.getElementById("mySidenav").style.width = "0px";
    document.getElementById("main").style.marginLeft = "0px";
    localStorage.setItem("menuState", "closed");
}

// Function to initialize the side menu state
function initMenuState() {
    const menuState = localStorage.getItem("menuState");
    const sidenav = document.getElementById("mySidenav");
    const main = document.getElementById("main");

    if (menuState === "open") {
        sidenav.style.width = "250px";
        main.style.marginLeft = "250px";
    } else {
        sidenav.style.width = "50px";
        main.style.marginLeft = "50px";
    }
}

// Initialize menu state when the page loads
document.addEventListener("DOMContentLoaded", initMenuState);
