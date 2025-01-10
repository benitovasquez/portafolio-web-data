// Aplica el tema antes de cargar el DOM
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
  document.documentElement.classList.add('dark-mode');
}

// Después, configura los eventos
document.addEventListener('DOMContentLoaded', () => {
  const themeSwitch = document.getElementById('theme-switch');
  const root = document.documentElement;

  // Sincroniza el estado del toggle con el tema guardado
  if (savedTheme === 'dark') {
    themeSwitch.checked = true;
  }

  // Escucha cambios en el toggle
  themeSwitch.addEventListener('change', () => {
    if (themeSwitch.checked) {
      root.classList.add('dark-mode');
      localStorage.setItem('theme', 'dark');
    } else {
      root.classList.remove('dark-mode');
      localStorage.setItem('theme', 'light');
    }
  });
});

// Agrega la clase 'loaded' después de aplicar el tema
document.documentElement.classList.add('loaded');
  