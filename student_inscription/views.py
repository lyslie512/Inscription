from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators  import login_required
from .forms import StudentForm,CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Faculty,Campus,Student
from django.views.generic.detail import DetailView
from django.views.generic import ListView,TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.utils.translation import gettext


# Create your views here.
def homes(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method=='POST':
			form=CreateUserForm(request.POST)
			if form.is_valid():
				user=form.save()
				auth_login(request,user)
			return redirect('login')
		else:

			form=CreateUserForm()
		return render(request,'home/home.html',{'form': form})

def login_page(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:

		if request.method == 'POST':
			username =request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request,username=username,password=password)

			if user is not None:
				login(request,user)
			return render(request,'home/home_page.html')
		else:
			messages.info(request,'Nom ou Mot de passe incorect')
	return render(request,'home/authentification.html')

def logout_page(request):
	logout(request)
	messages.info(request,"Deconnection reussit")
	return redirect('login')

@login_required()
def home_page(TemplateView):
	return render(request,'home/home_page.html')

class StudentCreate(CreateView):
	model=Student
	fields='__all__'
	template_name='create/student.html'

class StudentDetail(DetailView):
	context_object_name='student'
	model=Student
	template_name='detail/student.html'

	def get_object(self):
		student=super(StudentDetail,self).get_object()
		form=StudentForm(instance=student)
		return form

	def get_template_name(self):
		return['detail/student.html']
