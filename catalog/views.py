from django.shortcuts import render

# Create your views here.
from . import models


def showWordMenu(request):
    munus = models.WordMenu.objects.all()
    return render(request,'aside.html',{'menus' : munus})

def showPictureMenu(request):
    menus_one = models.PictureMenu.objects.filter(menulevel=1)
    menus_two = models.PictureMenu.objects.filter(menulevel=2)
    menus_three = models.PictureMenu.objects.filter(menulevel=3)
    menus_four = models.PictureMenu.objects.filter(menulevel=4)
    menus_five = models.PictureMenu.objects.filter(menulevel=5)
    menus_six = models.PictureMenu.objects.filter(menulevel=6)

    context = {
        'menus_one' : menus_one,
        'menus_two' : menus_two,
        'nenus_three' : menus_three,
        'nenus_four': menus_four,
        'nenus_five': menus_five,
        'nenus_six': menus_six,
    }

    return render(request,'aside.html',{'menus' : context})

def showVoiceMenu(request):
    munus = models.VoiceMenu.objects.all()
    return render(request,'aside.html',{'menus' : munus})

def showHomeMenu(request):
    homeMenus = models.HomeMenu.objects.all()
    return render(request,'aside.html',{'menus' : homeMenus})