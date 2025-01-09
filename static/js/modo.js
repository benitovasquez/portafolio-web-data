document.addEventListener('DOMContentLoaded', () => {
    const themeSwitch = document.getElementById('theme-switch');
    const root = document.documentElement;

    // Cambiar tema al hacer clic
    themeSwitch.addEventListener('click', () => {
        const isDarkMode = root.classList.toggle('dark-mode');
        localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');

        // Cambiar íconos del botón
        themeSwitch.classList.toggle('dark-mode');
    });

    // Mantener el tema al recargar
    if (localStorage.getItem('theme') === 'dark') {
        root.classList.add('dark-mode');
        themeSwitch.classList.add('dark-mode');
    }
});
