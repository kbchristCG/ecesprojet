from django.db import models


class Utilisateur(models.Model):
    nom = models.CharField("Nom de l'utilisateur", max_length=50)
    prenom = models.CharField("Prenom de l'utilisateur", max_length=50)
    genre = models.CharField("Genre de l'utilisateur", max_length=50)
    telephone = models.CharField("Téléphone de l'utilisateur", max_length=50)
    mot_de_passe = models.CharField("Mot de passe de l'utilisateur", max_length=50)

    def __str__(self) -> str:
        return self.nom
    
    def view_mot_de_passe(self):
        import base64
        return base64.b64encode(self.mot_de_passe.encode('utf-8'))
    