from django.shortcuts import render
from .models import UserProfile

def index(request):
    # Obtener el primer perfil
    try:
        profile = UserProfile.objects.first()
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'index.html', {"profile": profile})