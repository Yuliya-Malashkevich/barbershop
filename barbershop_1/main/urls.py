from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('services_for_women', views.services_for_women, name='services_for_women'),
    path('services_for_men', views.services_for_men, name='services_for_men'),
    path('manicure_pedicure', views.manicure_pedicure, name='manicure_pedicure'),
    path('services_for_children', views.services_for_children, name='services_for_children'),
    path('cosmetology_services', views.cosmetology_services, name='cosmetology_services'),
    path('gift_certificates', views.gift_certificates, name='gift_certificates'),
    path('reviews', views.reviews, name='reviews'), #отзывы
    path('add_review', views.add_review, name='add_review')

]