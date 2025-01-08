from django.shortcuts import render
from applications.index.models import UserProfile

def curriculum(request):
    try:
        profile = UserProfile.objects.first()
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'curriculum.html', {"profile": profile})