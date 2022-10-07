from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm  

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
    

def login(request):  
    if request.POST == 'POST':  
        form = UserCreationForm()  
        if form.is_valid():  
            form.save()  
    else:  
        form = UserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'includes/login.html', context)