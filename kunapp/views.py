from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')


def classy(request):
    return render(request, 'classy.html')


def blog(request):
    return render(request, 'blog.html')
# Create your views here.
