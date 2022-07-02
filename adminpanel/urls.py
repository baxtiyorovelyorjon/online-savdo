from django.urls import path
from adminpanel import views


urlpatterns =[
    path('register',views.register,name='register'),
    path('login_form',views.login_form,name='login_form'),
]