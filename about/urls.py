from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.view_contact, name='view_contact'),
    path('faqs/', views.view_faqs, name='view_faqs'),
    path('about/', views.view_about, name='view_about'),
]