from django.http import HttpResponse
from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.files.storage import default_storage
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout




# Create your views here.

def index(request):
    projets = Project.objects.all()
    return render(request,'home.html' , {'projets': projets})

def listeProjets(request):
    projets = Project.objects.all()
    return render(request, 'portfolio.html', {'projets': projets})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services' : services} )

def equipe(request):
    personnes = Personne.objects.all()
    return render(request, 'equipe.html', {'personnes' : personnes})

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        telephone = request.POST.get("phone")
        message = request.POST.get("message")
        contact = Contact.objects.create(name = nom , email = email , phone = telephone , message=message)
    return render(request, 'contact.html')

def inscription(request):
    if request.method == 'POST':
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        mdp = request.POST.get("mdp")
        utilisateur = User.objects.create_user(username = nom , email = email , password=mdp)
    return render(request, 'inscription.html')


@login_required
def DemandeProjet(request):
    if request.method == 'POST':
        nom = request.POST.get("nom")
        description = request.POST.get("description")
        image = request.FILES.get('image')
        projet = Project.objects.create(nom = nom , description = description , image= image)
    return render(request, 'demandeProjet.html')


def deconnexion(request):
    logout(request)
    return redirect('/')



