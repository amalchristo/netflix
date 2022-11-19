from django.urls import path,include
from . import views
app_name='homepg'

urlpatterns = [
    path('', views.home,name='home'),
    path('movies', views.movies,name='movie'),
]