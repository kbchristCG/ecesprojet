from django.shortcuts import redirect, render, resolve_url
from .models import Utilisateur


def accueil(request):
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'home.html', {'utilisateurs':utilisateurs})


def se_connecter(request):
    return render(request, 'login.html')


def enregistrement(request):
    data = request.POST
    utilisateur = Utilisateur.objects.create(
        nom=data.get('nom'),
        prenom=data.get('prenom'),
        genre=data.get('genre'),
        telephone=data.get('telephone'),
        mot_de_passe=data.get('password'),
        )
    utilisateur.save()
    return redirect('home')


def modification(request,**matricule):
    import base64
    data = request.POST
    id = matricule['id']
    utilisateur = Utilisateur.objects.get(id=id)
    if request.method == 'POST':
        utilisateur.nom = data.get('nom', utilisateur.nom)
        utilisateur.prenom = data.get('prenom', utilisateur.prenom)
        utilisateur.genre = data.get('genre', utilisateur.genre)
        utilisateur.telephone = data.get('telephone', utilisateur.telephone)
        # utilisateur.mot_de_passe = data.get('password', utilisateur.mot_de_passe)
        utilisateur.save()
        return redirect('home')
    return render(request, 'edit.html', {'utilisateur':utilisateur})


def supprimer(request, **matricule):
    id = matricule['id']
    utilisateur = Utilisateur.objects.get(id=id)
    utilisateur.delete()
    return redirect('home')