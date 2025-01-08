from django.shortcuts import render

def curriculum(request):
    return render(request, 'curriculum/curriculum.html')