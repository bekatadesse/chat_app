from django.shortcuts import render, redirect

# Create your views here.

def frontpage(request):
    return render(request, 'core/index.html')
