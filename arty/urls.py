from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services,name="services"),
    path('equipe/', views.equipe,name="equipe"),
    path('contact/', views.contact ,name="contact"),
    path('listeProjets/', views.listeProjets, name='listeProjets'),
    path('DemandeProjet/', views.DemandeProjet, name='DemandeProjet'),
    path('inscription/', views.inscription, name='inscription'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    
    

    
]
