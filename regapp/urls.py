
from django.urls import path
from .import views

urlpatterns = [

    path('',views.insert,name='registration'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('view/',views.view,name='view'),
    path('detailview/<str:pk>',views.detailview,name='detailview'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('alogin/',views.alogin,name='alogin'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('display/',views.display,name='display'),
    path('logout/',views.logoutuser,name='logout'),
   
]
