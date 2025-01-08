from django.shortcuts import render

def sobre_mi(request):
    return render(request, 'sobremi/sobre-mi.html')
