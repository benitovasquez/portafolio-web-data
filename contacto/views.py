from django.shortcuts import render
from index.models import UserProfile

def contacto(request):
    try:
        profile = UserProfile.objects.first()
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'contacto.html', {"profile": profile})