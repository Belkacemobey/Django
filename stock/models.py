from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    quantite = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    seuil_alerte = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.nom
