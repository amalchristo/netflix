from django.urls import path
from . import views
app_name='clints'

urlpatterns = [
    path('', views.index,name='intex'),
]