from django.shortcuts import render, redirect
from mhz.models import data4
from django.contrib import messages
from django.http import HttpResponseRedirect


def main(request):
    return render(request, 'mhz/main.html')

def login(request):
    return render(request, 'mhz/login.html')



def profile(request):
    if request.method=='POST':
        if data4.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            data = data4.objects.get(email=request.POST['email'], password=request.POST['password'])
            return render(request, 'mhz/profile.html', {'member': data})
        else:
            return render(request, 'mhz/login.html')



def index(request):
    datas = data4.objects.all()
    context = {'members': datas}
    return render(request, 'mhz/index.html', context)

def create(request):
    Datas = data4(Name=request.POST['name'], Age=request.POST['age'],
                   Qualification=request.POST['Qualification'], Yearofpass=request.POST['Yearofpass'],
                   mobile=request.POST['mobile'], email=request.POST['email'], password=request.POST['password'],
                   post = request.POST['post'], experience=request.POST['experience'])
    Datas.save()
    return redirect('/')
