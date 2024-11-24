// Function to open the side menu
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    // Save the menu state in localStorage
    localStorage.setItem("menuState", "open");
}

// Function to close the side menu
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    // Save the menu state in localStorage
    localStorage.setItem("menuState", "closed");
}

// Function to initialize the side menu state
function initMenuState() {
    const menuState = localStorage.getItem("menuState");
    if (menuState === "open") {
        // Open the menu if the state is "open"
        openNav();
    }
}

// Initialize menu state when the page loads
document.addEventListener("DOMContentLoaded", initMenuState);
