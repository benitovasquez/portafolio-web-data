from django.shortcuts import render
from applications.index.models import UserProfile

def sobre_mi(request):
    try:
        profile = UserProfile.objects.first()
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'sobre-mi.html', {"profile": profile})
