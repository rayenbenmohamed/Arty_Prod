from django.db import models
from datetime import datetime
from django.db import models


class Service(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Project(models.Model):
    STATUS = {("Achevé","Achevé") , ("Demandé","Demandé") , ("En Cours","En Cours") }
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateTimeField(default=datetime.now , blank=True)
    date_fin = models.DateTimeField(default=datetime.now , blank=True)
    image = models.ImageField(upload_to='images/')
    status = models.CharField(choices=STATUS, max_length=50 , default="Demandé" ) 

    def __str__(self):
        return self.nom

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

class Personne(models.Model):
    nom = models.CharField( max_length=50)
    cv = models.FileField(upload_to=None, max_length=100)
    photo = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    linkedin = models.URLField( max_length=200)
    

    def __str__(self):
        return self.nom
    


