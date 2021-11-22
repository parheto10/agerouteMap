from django.db import models
from django.contrib.auth.models import User

class Concessionaire(models.Model):
    libelle = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    site_internet = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return ("%s") %(self.libelle)

    class Meta:
        verbose_name_plural = "CONCESSIONNAIRES"
        verbose_name = "concessionaire"
        ordering = ["libelle"]

    def save(self, force_insert=False, force_update=False):
        self.libelle = self.libelle.upper()
        super(Concessionaire, self).save(force_insert, force_update)

class Ville(models.Model):
    libelle = models.CharField(max_length=255)

    def __str__(self):
        return ("%s") %(self.libelle)

    def save(self, force_insert=False, force_update=False):
        self.libelle = self.libelle.upper()
        super(Ville, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "VILLES"
        verbose_name = "villes"
        ordering = ["libelle"]

class Commune(models.Model):
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=255)

    def __str__(self):
        return ("%s - %s") % (self.libelle, self.ville.libelle)

    def save(self, force_insert=False, force_update=False):
        self.libelle = self.libelle.upper()
        super(Commune, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "COMMUNES"
        verbose_name = "commune"
        ordering = ["libelle"]

class Locale(models.Model):

    Equipement = (
        ('FO_CUIVRE', 'FO/PAIRES DE CUIVRE'),
        ('FO', 'FO')
    )
    #user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    concessionnaire = models.ForeignKey(Concessionaire, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=255)
    type_equipement = models.CharField(max_length=50, choices=Equipement, default='CUIVRE')
    profondeur_cable = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    latitude = models.CharField(max_length=10, null=True, blank=True)
    longitude = models.CharField(max_length=12, null=True, blank=True)
    chbre_proche = models.ForeignKey("locale", on_delete=models.CASCADE, blank=True, null=True,related_name="locale_proches")
    dtce_chambre_proche = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return ('%s - %s') %(self.libelle, self.concessionnaire.libelle)

    def save(self, force_insert=False, force_update=False):
        self.libelle = self.libelle.upper()
        self.type_equipement = self.type_equipement.upper()
        super(Locale, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "CHAMBRES TECHNIQUES"
        verbose_name = "chambre technique"
        ordering = ["libelle"]


# Create your models here.
