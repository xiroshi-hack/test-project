from django.shortcuts import redirect, render, reverse
from django.views import generic
from .models import *
from rate.forms import Registration
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
    

    
    
    
class Main(generic.TemplateView):
    template_name = 'index.html'
    

class Register(generic.CreateView):
    template_name = 'includes/login.html'
    form_class = Registration
    
    def get_success_url(self):
        return reverse('core:home')