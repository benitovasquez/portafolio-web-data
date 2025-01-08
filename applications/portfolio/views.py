from django.shortcuts import render
from applications.index.models import UserProfile

def portafolio(request):
    try:
        profile = UserProfile.objects.first()
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'portafolio.html', {"profile": profile})

