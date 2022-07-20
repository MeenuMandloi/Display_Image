from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register, name='Register'),
    path('', views.login, name="login"),
    path('update/<int:id>',views.update, name="update"),

]
