from django.shortcuts import render
from .models import Project

def portfolio(request):
    label = request.GET.get('label')  # Obtiene el filtro desde la URL
    if label:
        projects = Project.objects.filter(label=label)  # Filtra los proyectos por etiqueta
    else:
        projects = Project.objects.all()  # Muestra todos los proyectos si no hay filtro
    return render(request, 'portfolio/portafolio.html', {'projects': projects})
