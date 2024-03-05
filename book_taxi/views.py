from django.shortcuts import render
from django.http import HttpResponse
from book_taxi.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
# from django.contrib.auth import logout, authenticate, login as l 
from django.core.mail import send_mail
from django.core.mail import EmailMessage, get_connection
from django.conf import settings




# Create your views here.
def sendmail_booking(request):
    
    if request.method == "POST":
        name = request.POST['name']
        cartype = request.POST['cars']
        pickup = request.POST['pickup']
        drop = request.POST['drop']
        mobail = request.POST['mobail']
        
    full_message = f"""
        Received message below from {name}
        
        .....................................
        
        car type : {cartype}
        pickup : {pickup}
        drop : {drop}
        mobail no : {mobail}
    """
    send_mail(
        "Receve booking details from yashtaxi",
        full_message,
        'yashtaxi2000@gmail.com',
        ['rutukotadiya999@gmail.com'],
        fail_silently=False,
        
        
          
    )
    messages.success(request, " your information send succsessfully ")
    return redirect('index')

def sendmail_contact(request):
    
    if request.method == "POST":
        name = request.POST['name']
        mobail = request.POST['mobail']
        message = request.POST['message']
        
    full_message = f"""
        Received message below from {name}
        
        .....................................
        
        massage : {message}
        mobail no : {mobail}
    """
    send_mail(
        "Receve contact details from yashtaxi",
        full_message,
        'yashtaxi2000@gmail.com',
        ['rutukotadiya999@gmail.com'],
        fail_silently=False,
          
    )
    messages.success(request, " your information send succsessfully ")
    
    return redirect('contact')
    
    
    

def index(request):
    """ For index page..."""
    
    
    return render(request, 'index.html')

def about(request):
    """ For about page...."""
    
    
    
    return render(request, 'about.html')

def contact(request):
    """ For contact page...."""
    
    
    return render(request, 'contact.html')

def service(request):
    """ For service page..."""
    
    
    return render(request, 'service.html')