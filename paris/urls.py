"""paris URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('test', views.home),
    path('equipe/<int:id_equipe>',views.equipe, name='mon_equipe'),
    path('dateActuelle',views.date_actuelle, name='date'),
    path('login', views.connexion, name='login'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('',views.hub, name='hub'),
]
