document.addEventListener("DOMContentLoaded", () => {
  const niveles = ['Básico', 'Inicial', 'Intermedio', 'Avanzado', 'Experto'];

  document.querySelectorAll(".studie-level").forEach(level => {
    let tooltip;

    level.addEventListener("mouseenter", (e) => {
      const filledCount = level.querySelectorAll(".circle.filled").length;
      const texto = `Nivel: ${niveles[filledCount - 1] || 'Desconocido'}`;

      tooltip = document.createElement("div");
      tooltip.className = "tooltip-tooltip";
      tooltip.textContent = texto;
      document.body.appendChild(tooltip);
    });

    level.addEventListener("mousemove", (e) => {
      if (tooltip) {
        tooltip.style.left = e.pageX + 15 + "px";
        tooltip.style.top = e.pageY + 15 + "px";
      }
    });

    level.addEventListener("mouseleave", () => {
      if (tooltip) {
        tooltip.remove();
        tooltip = null;
      }
    });
  });
});
