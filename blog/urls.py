from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero, name='hero'),
    path('post/<int:id>/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]
