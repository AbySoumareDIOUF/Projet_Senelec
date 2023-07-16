from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')



def register(request):
    if request.method =="POST":
        Nom =request.POST['Nom']
        Prenom =request.POST['Prenom']
        Adresse_Email =request.POST['Adresse Email']
        Mot_de_passe=request.POST['Mot de passe']
        Confirmez_votre_Mot_de_passe =request.POST['Confirmez votre Mot de passe']
        mon_utilisateur =User.objects.create_user(Nom,Prenom,Adresse_Email)
        mon_utilisateur.Nom=Nom
        mon_utilisateur.Prenom=Prenom
        mon_utilisateur.Adresse_Email= Adresse_Email
        mon_utilisateur.save()
        messages.success=(request,'Inscription validée')
        return redirect('login')
        
        
    return render(request,'register.html')

def login(request):
    if request.method =="POST":
         Adresse_Email=request.POST['Adresse_EmAdresse_Email']
         Mot_de_passe=request.POST['Mot de passe']
         User =authenticate(Adresse_Email=Adresse_Email, Mot_de_passe=Mot_de_passe)
         if User is not None:
             login(request,User)
             Nom=User.Nom
             return render(request,'login.html',{'Nom'==Nom})
         else:
             messages.error(request,'mauvaise authentification')
             return redirect('login')
    return render(request,'login.html')

    



