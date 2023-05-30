from django.shortcuts import render
from django.http import HttpResponse
from bmi.models import People, Level
from .forms import PeopleModelForm

def setBMI(p):
    p.bmi = round(p.w/(p.h/100)**2, 2)

def home(request):
    print('request: ', request)
    pList = People.objects.all()
    print('pList: ', pList)

    for p in pList:
        # p.bmi = round(p.w/(p.h/100)**2, 2)
        setBMI(p)
        print('After adding bmi to p: ', p, p.bmi)

    param = {
        'plist': pList
    }
    return render(request, 'peoples.html', context=param)

def detail(request, id):
    p = People.objects.get(id=id)
    p.bmi = round(p.w/(p.h/100)**2, 2)
    print('p.photo.url: ', p.photo.url)

    param = {
        'p': p
    }
    return render(request, 'details.html', context=param)

def update(request, id):
    # POST
    if request.method == "POST":
        p = People.objects.get(id = id)
        if p: 
            form = PeopleModelForm(request.POST, instance = p)
            if form.is_valid():
                form.save()
                print ('form saved')
                setBMI(p)
                return render(request, "details.html", {'p': p}) 
            else: 
                return render(request, "find_fail.html", {'error_msg': str(form.errors)}) 
        else:
            print ('form.errors: ', form.errors)
            return render(request, "find_fail.html", {'error_msg': 'ID not found'}) 
    
    # GET, generate a form and pass to update_people.html
    p = People.objects.get(id=id)
    if p: 
        form = PeopleModelForm(instance = p)    
        context = {'form':form}     
        return render(request, "update_people.html", context)
    else:
        return render(request, "find_fail.html", {'error_msg': 'ID not found'})             
