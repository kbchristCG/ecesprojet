from django.urls import path
from .views import accueil, se_connecter,supprimer, modification, enregistrement


urlpatterns = [
    path('', accueil, name='home'),
    path('se_connecter', se_connecter, name='login'),
    path('enregistrement', enregistrement, name='enregistrement'),
    path('modification/<int:id>', modification, name='edit'),
    path('supprimer/<int:id>', supprimer, name='supprimer'),
]
