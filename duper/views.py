from django.shortcuts import render


def render_B(request):
    return render(request, 'duper/b.html')


def render_C(request):
    return render(request, 'duper/c.html')
