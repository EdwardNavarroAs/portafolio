from django.shortcuts import render

# ========================
# VISTA PRINCIPAL (Home)
# ========================

# Vista principal del sitio web, accesible en la raíz "/".
# Esta vista está enlazada a la URL "" (vacía) en miweb/urls.py.
# Renderiza la plantilla 'miweb/home.html'.
# Gracias al context processor definido, esta vista ya tiene acceso automático
# al título del sitio y a los elementos de navegación (navbar_items).
def home(request):
    return render(request, 'miweb/home.html')


# ========================
# VISTA DE ESTUDIOS
# ========================

# Vista para la sección "Estudios", accesible en "/studies/".
# Renderiza la plantilla 'miweb/studies.html'.
# Puedes agregar un contexto adicional en el futuro si deseas mostrar datos
# como estudios académicos, cursos, certificaciones, etc.
def studies(request):
    return render(request, 'miweb/studies.html')


# ========================
# VISTA DE PORTAFOLIO
# ========================

# Vista para la sección "Portafolio", accesible en "/portfolio/".
# Renderiza la plantilla 'miweb/portfolio.html'.
# Es ideal para mostrar los proyectos personales o profesionales en los que has trabajado.
# También se puede enriquecer con datos dinámicos si luego decides usar modelos o base de datos.
def portfolio(request):
    return render(request, 'miweb/portfolio.html')
