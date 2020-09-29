from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.
class Faculty(models.Model):
	name=models.CharField(max_length=40,verbose_name= _("name"))

	def __str__(self):
		return self.name

class Campus(models.Model):
	name=models.CharField(max_length=50,verbose_name=_("name"))

	def __str__(self):
		return self.name

class Student(models.Model):
	name=models.CharField(max_length=50,verbose_name=_("Name"))
	first_name=models.CharField(max_length=30,verbose_name=_("First name"))
	date=models.DateField(verbose_name=_("Date"))
	nationality=models.CharField(max_length=100,verbose_name=_("Nationality"))
	sex=models.CharField(max_length=20,verbose_name=_("Sex"))
	civil_status=models.CharField(max_length=30,verbose_name=_("Civil status"))
	diploma=models.CharField(max_length=50,verbose_name=_("Diploma"))

	facult=models.ForeignKey('student_inscription.Faculty',on_delete=models.CASCADE, related_name='faculty',verbose_name=_("Faculty"))

	level=models.CharField(max_length=50,verbose_name=_("level"))

	campus=models.ForeignKey('student_inscription.Campus',on_delete=models.CASCADE,related_name='campus',verbose_name=_("campus"))

	cni=models.CharField(max_length=40,verbose_name=_("Identity card number"))
	email=models.CharField(max_length=50,verbose_name=_("Email"))
	phone=models.IntegerField(verbose_name=_("Phone number"))


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('detailstudent', kwargs={'pk': self.pk})


