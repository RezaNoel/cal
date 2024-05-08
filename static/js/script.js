// script.js

// Get references to sidebar and toggle button
const sidebar = document.getElementById('sidebar');
const toggleSidebar = document.getElementById('toggleSidebar');
const toggleMobileMenu = document.getElementById('toggleMobileMenu');

// Toggle sidebar function
function toggleSidebarVisibility() {
    sidebar.classList.toggle('hidden');
}

// Event listener for toggle sidebar button
toggleSidebar.addEventListener('click', toggleSidebarVisibility);

// Event listener for toggle mobile menu button
toggleMobileMenu.addEventListener('click', toggleSidebarVisibility);
