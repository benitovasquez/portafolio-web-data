document.addEventListener('DOMContentLoaded', () => {
  const themeSwitch = document.getElementById('theme-switch');
  const root = document.documentElement;

  // Detectar si venimos con 'dark-mode' agregado en el <html>
  const isDark = root.classList.contains('dark-mode');
  themeSwitch.checked = isDark;

  // Escuchar cambios del checkbox
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

