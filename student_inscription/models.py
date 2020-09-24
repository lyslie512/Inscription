from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Faculty(models.Model):
	name=models.CharField(max_length=40,verbose_name="Nom Falcute")

	def __str__(self):
		return self.name

class Campus(models.Model):
	name=models.CharField(max_length=50,verbose_name="Nom du campus")

	def __str__(self):
		return self.name

class Student(models.Model):
	name=models.CharField(max_length=50,verbose_name="Nom")
	first_name=models.CharField(max_length=30,verbose_name="Prenom")
	date=models.DateField(verbose_name="Date de naissance")
	nationality=models.CharField(max_length=100,verbose_name="Nationalite")
	sex=models.CharField(max_length=20,verbose_name="Sex")
	civil_status=models.CharField(max_length=30,verbose_name="Etat civil")
	diploma=models.CharField(max_length=50,verbose_name="Diplome")
	facult=models.ForeignKey(Faculty,on_delete=models.CASCADE, related_name='faculty',verbose_name="Faculte")
	level=models.CharField(max_length=50,verbose_name="Niveau")
	campus=models.ForeignKey(Campus,on_delete=models.CASCADE,related_name='campus',verbose_name="Campus")
	cni=models.CharField(max_length=40,verbose_name="Carte d'identite")
	email=models.CharField(max_length=50,verbose_name="Adresse email")
	phone=models.IntegerField(verbose_name="Numero de telephone")


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('detailstudent', kwargs={'pk': self.pk})


