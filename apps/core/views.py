from django.shortcuts import render

def frontpage(request):
    return render(request, 'core/frontpage.html')

def register(request):
     return render(request, 'core/register.html')

