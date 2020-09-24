from django.urls import path
from student_inscription import views
from student_inscription.views import (
	StudentCreate,StudentDetail,
	)


urlpatterns = [
    path('',views.homes,name='home'),
    path('login/',views.loginPage,name='login'),
    path('home/',views.home_page,name='home_page'),
    path('logout/',views.logout_Page,name='logout'),
    path('student/',StudentCreate.as_view(),name='student'),
    path('detailstudent/<pk>/',StudentDetail.as_view(),name='detailstudent'),

]