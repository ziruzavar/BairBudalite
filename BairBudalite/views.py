from django.shortcuts import render

from BairBudalite.models import Pohodi, Budali, Images


def index(request):
    context = {
        'pohodi': Pohodi.objects.all().order_by('-id')[:3],
        'budali': Budali.objects.all().order_by('-id')[:4:-1],
    }
    return render(request, 'index.html', context)


def pohodi(request):
    context = {
        'pohodi': Pohodi.objects.all()
    }
    return render(request, 'generic.html', context)


def elements(request):
    return render(request, 'elements.html')


def pohod(request, pk):
    pohod = Pohodi.objects.get(pk=pk)
    context = {
        'pohod': pohod,
        'images': Images.objects.filter(pohod=pk).all()
    }
    return render(request, 'pohod.html', context)