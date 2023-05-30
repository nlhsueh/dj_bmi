from django.shortcuts import render
from django.http import HttpResponse
from bmi.models import People, Level

# Create your views here.


def home(request):
    print('request: ', request)
    pList = People.objects.all()
    print('pList: ', pList)

    for p in pList:
        p.bmi = round(p.w/(p.h/100)**2, 2)
        print('After adding bmi to p: ', p, p.bmi)

    param = {
        'plist': pList
    }
    return render(request, 'peoples.html', context=param)


def detail(request, id):
    p = People.objects.get(id=id)
    p.bmi = round(p.w/(p.h/100)**2, 2)
    # print('p.photo.url: ', p.photo.url)

    param = {
        'p': p
    }
    return render(request, 'details.html', context=param)
