// General function to handle modal opening and closing
function setupModal(modalId, openButtonClass, closeButtonId) {
    const modal = document.getElementById(modalId);
    const openButtons = document.querySelectorAll(`.${openButtonClass}`);
    const closeButton = document.getElementById(closeButtonId);

    if (!modal || !openButtons.length || !closeButton) {
        console.error(`Modal setup failed for modalId: ${modalId}`);
        return;
    }

    // Open modal
    openButtons.forEach((button) => {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            modal.style.display = "flex"; // Use 'flex' for proper alignment if necessary
        });
    });

    // Close modal
    closeButton.addEventListener("click", () => {
        modal.style.display = "none";
    });

    // Close modal when clicking outside the modal content
    window.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
}

// Apply the modal logic for both the "Add Bus" and "Add Employee" modals
setupModal("addBusModal", "add-btn", "closeModalButton"); // For "Add New Bus" modal
setupModal("addEmployeeModal", "openAddEmployeeModal", "closeAddEmployeeModal"); // For "Add New Employee" modal
