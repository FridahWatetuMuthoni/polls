from django.urls import path 
from . import views

urlpatterns = [
    path("",views.home, name='home'),
    path("create/",views.create, name="create"),
    path("results/<int:pk>/", views.results, name='results'),
    path("vote/<int:pk>/", views.vote, name='vote')
]
