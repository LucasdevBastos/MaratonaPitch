from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # nova tela inicial
    path('startups/', views.lista_startups, name='lista_startups'),
    path('startup/<int:pk>/', views.detalhe_startup, name='detalhe_startup'),
    path('startup/<int:pk>/votar/', views.votar_startup, name='votar_startup'),
    path('startup/<int:pk>/comentar/', views.comentar_startup, name='comentar_startup'),
    path('dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('gestao/startups/nova/', views.criar_startup, name='criar_startup'),
]
