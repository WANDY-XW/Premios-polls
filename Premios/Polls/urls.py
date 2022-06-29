from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
      path('', views.Index, name='index'),
      path('<int:question>/', views.Detalle, name='detalle'),
      path('vote/<int:question>/', views.Vote, name='vote'),
      path('<int:question>/', views.Resultados, name='resultados'),
]
