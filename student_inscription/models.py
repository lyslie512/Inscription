from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Faculty(models.Model):
	name=models.CharField(max_length=40,verbose_name="name")

	def __str__(self):
		return self.name

class Campus(models.Model):
	name=models.CharField(max_length=50,verbose_name="name")

	def __str__(self):
		return self.name

class Student(models.Model):
	name=models.CharField(max_length=50,verbose_name="Name")
	first_name=models.CharField(max_length=30,verbose_name="First name")
	date=models.DateField(verbose_name="Date")
	nationality=models.CharField(max_length=100,verbose_name="Nationality")
	sex=models.CharField(max_length=20,verbose_name="Sex")
	civil_status=models.CharField(max_length=30,verbose_name="Civil status")
	diploma=models.CharField(max_length=50,verbose_name="Diploma")

	facult=models.ForeignKey('student_inscription.Faculty',on_delete=models.CASCADE, related_name='faculty',verbose_name="Faculty")

	level=models.CharField(max_length=50,verbose_name="level")

	campus=models.ForeignKey('student_inscription.Campus',on_delete=models.CASCADE,related_name='campus',verbose_name="campus")

	cni=models.CharField(max_length=40,verbose_name="Identity card number")
	email=models.CharField(max_length=50,verbose_name="Email")
	phone=models.IntegerField(verbose_name="Phone number")


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('detailstudent', kwargs={'pk': self.pk})


