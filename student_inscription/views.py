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
from django.views import View


# Create your views here.
class register_page(View):
	form_class=CreateUserForm
	template_name='home/home.html'

	def get(self, request, *args, **kwargs):
		form=self.form_class
		return render(request, self.template_name, {'form': form })

	def post(self,request, *args , **kwargs):
		form=self.form_class(request.POST)
		if form.is_valid():
				user = form.save()
				auth_login(request,user)
		return redirect('login')
		return render(request, self.template_name, {'form': form })

class login_page(View):
	template_name='home/authentification.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name) #{'form': form })

	def post(self,request, *args, **kwargs):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
		return render(request,'home/home_page.html')



def logout_page(request):
	logout(request)
	messages.info(request,"Deconnection reussit")
	return redirect('login')

@login_required()
def home_page(request):
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
