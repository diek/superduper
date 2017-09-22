from django.shortcuts import render


def no_super(request):
    return render(request, 'duper/no_super.html')


def super(request):
    return render(request, 'duper/super.html')
