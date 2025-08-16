from django.shortcuts import render


def index(request):
    # You can pass data into the template here later if you want
    return render(request, "pages/index.html")
