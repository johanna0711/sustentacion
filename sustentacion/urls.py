"""sustentacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from core import views

urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('portada/', views.portada, name="portada"),
    url('usuario/',include('usuario.urls')),
    path('', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('MyV/', views.MyV, name="MyV"),
    path('curso/', views.curso, name="curso"),
    path('modificarcurso/<int:pk>', views.modificarcurso, name="modificarcurso"),
    path('crearcurso/', views.crearcurso, name="crearcurso"),
    path('eliminarcurso/<int:id>', views.eliminarcurso, name="eliminarcurso"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('modificarestudiante/<int:pk>', views.modificarestudiante, name="modificarestudiante"),
    path('crearestudiante/', views.crearestudiante, name="crearestudiante"),
    path('eliminarestudiante/<int:pk>', views.eliminarestudiante, name="eliminarestudiante"),
    path('familia/', views.familia, name="familia"),
    path('modificarfamilia/<int:pk>', views.modificarfamilia, name="modificarfamilia"),
    path('crearfamilia/', views.crearfamilia, name="crearfamilia"),
    path('eliminarfamilia/<int:pk>', views.eliminarfamilia, name="eliminarfamilia"),
    path('enfermedades/', views.enfermedades, name="enfermedades"),
    path('modificarenfermedad/<int:pk>', views.modificarenfermedad, name="modificarenfermedad"),
    path('crearenfermedad/', views.crearenfermedad, name="crearenfermedad"),
    path('eliminarenfermedad/<int:pk>', views.eliminarenfermedad, name="eliminarenfermedad"),
    path('retiro/', views.retiro, name='retiro'),
    path('modificarretiro/<int:pk>', views.modificarretiro, name="modificarretiro"),
    path('crearretiro/', views.crearretiro, name="crearretiro"),
    path('eliminarretiro/<int:pk>', views.eliminarretiro, name="eliminarretiro"),
    path('formulario/', views.formulario, name="formulario"),
    path('modificarformulario/<int:pk>', views.modificarformulario, name="modificarformulario"),
    path('crearformulario/', views.crearformulario, name="crearformulario"),
    path('eliminarformulario/<int:pk>', views.eliminarformulario, name="eliminarformulario"),
    path('general/', views.general, name="general"),
    path('modificargeneral/<int:pk>', views.modificargeneral, name="modificargeneral"),
    path('creargeneral/', views.creargeneral, name="creargeneral"),
    path('eliminargeneral/<int:pk>', views.eliminargeneral, name="eliminargeneral"),
    path('admin/', admin.site.urls),
]