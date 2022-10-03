from django.shortcuts import render
from .models import *

def home(request):    
    
    text = Title.objects.all()
    abaut = Abaout.objects.all()
    expertises = Expertises.objects.all()
    product = Products.objects.all()
    testmonials = Testmonials.objects.all()
    
    
    return render(request, 'pages/home.html', {
        'text': text,
        'abaut': abaut,
        'expertises': expertises,
        'product': product,
        'testmonials': testmonials,
    })