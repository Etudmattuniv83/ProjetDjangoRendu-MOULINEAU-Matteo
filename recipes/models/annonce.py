from django.db import models

class Annonce(models.Model):
    titre = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    prix = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.CharField(max_length=1000)
    date_debut = models.DateTimeField("Created At", auto_now_add=True)
    vendeur_nom = models.CharField(max_length=120)
    vendeur_telephone = models.CharField(max_length=20)
    vendeur_ville = models.CharField(max_length=300)
    def _str_(self):
        return self.titre
