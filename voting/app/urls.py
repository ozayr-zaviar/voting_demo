from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:candidate_id>', views.vote, name='vote'),
    path('results', views.result, name='result')
]

