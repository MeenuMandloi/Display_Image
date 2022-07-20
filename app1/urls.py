from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register/', views.Register, name='Register'),
    path('login/', views.login, name="login"),

]
