from django.shortcuts import render

# Create your views here.
def sobre_mi(request):
    return render(request, 'sobre-mi.html')
