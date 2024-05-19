from django.shortcuts import render

def landing(request):
    """
    Landing page
    """
    return render(request, "core/landing.html")