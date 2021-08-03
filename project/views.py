from django.shortcuts import render


def projectHome(request):
    return render(request, 'project/index.html')
