document.addEventListener("DOMContentLoaded", function () {
    // Evita que el navegador recuerde el scroll anterior
    if ('scrollRestoration' in history) {
        history.scrollRestoration = 'manual';
    }

    // Fuerza el scroll hacia la parte superior al cargar
    window.scrollTo(0, 0);

    // Espera un poco para asegurar que todo esté renderizado antes de observar
    setTimeout(() => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                }
            });
        }, {
            threshold: 0.3 // activa cuando el 30% del elemento es visible
        });

        document.querySelectorAll(".scroll-fade").forEach(el => observer.observe(el));
    }, 50); // Delay para mayor compatibilidad
});
