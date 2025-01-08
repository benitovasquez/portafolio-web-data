from django.shortcuts import render
from applications.index.models import UserProfile

def blog(request):
    try:
        profile = UserProfile.objects.first()
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'blog.html', {"profile": profile})