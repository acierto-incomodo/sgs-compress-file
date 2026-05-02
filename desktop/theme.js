function setTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
}

// Detecta sistema automáticamente
function detectTheme() {
  const dark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  setTheme(dark ? "dark" : "light");
}

// Escucha cambios del sistema en vivo
window.matchMedia("(prefers-color-scheme: dark)")
  .addEventListener("change", detectTheme);

detectTheme();