from django.contrib import admin
from .models import Project, Tag

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'label', 'date')  # Mostrar estos campos en la lista
    list_filter = ('label', 'date')           # Filtros laterales por categoría y fecha
    search_fields = ('title', 'description')  # Búsqueda por título y descripción
    filter_horizontal = ('sublabels',)        # Selector horizontal para subetiquetas

admin.site.register(Tag)  # Registrar el modelo Tag (sublabels)
admin.site.register(Project, ProjectAdmin)  # Registrar el modelo Project con configuraciones
