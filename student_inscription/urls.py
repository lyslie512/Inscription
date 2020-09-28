from django.urls import path
from student_inscription import views
from django.views import View
from student_inscription.views import (
	register_page,login_page,
	StudentCreate,StudentDetail
	)


urlpatterns = [
    path('',register_page.as_view(),name='register_page'),
    path('login/',login_page.as_view(),name='login'),
    path('home/',views.home_page,name='home'),
    path('logout/',views.logout_page,name='logout'),
    path('student/',StudentCreate.as_view(),name='student'),
    path('detailstudent/<pk>/',StudentDetail.as_view(),name='detailstudent'),

]