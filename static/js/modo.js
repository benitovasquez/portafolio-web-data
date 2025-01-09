document.addEventListener('DOMContentLoaded', () => {
    const themeSwitch = document.getElementById('theme-switch');
    const root = document.documentElement;
  
    // Verifica si el usuario tenía un tema seleccionado en localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
      root.classList.add('dark-mode');
      themeSwitch.checked = true;  // Mueve el toggle a la derecha
    }
  
    // Al cambiar el estado del checkbox
    themeSwitch.addEventListener('change', () => {
      if (themeSwitch.checked) {
        // Activar modo oscuro
        root.classList.add('dark-mode');
        localStorage.setItem('theme', 'dark');
      } else {
        // Activar modo claro
        root.classList.remove('dark-mode');
        localStorage.setItem('theme', 'light');
      }
    });
  });
  