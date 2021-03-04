from django.contrib import admin
from django.urls import path
from Views.HomeView import HomeView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),
    path('formulario/', HomeView.formularioAlumnos, name='formularioAlumnos'),

]
