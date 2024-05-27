from django.urls import  path
from . import views

urlpatterns = [
    path('cities/', views.city_list, name='city_list'),
    path('cities/<str:city>/locations/', views.location_list, name='location_list'),
    path('hospitals/<int:hospital_id>/', views.hospital_detail, name='hospital_detail'),
]