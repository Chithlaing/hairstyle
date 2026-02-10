from django.urls import path
from . import views

urlpatterns = [
    path('', views.hairstyle, name='design-hairstyle'),
    path('about/', views.about, name='design-about'),
    path('hairdesign/', views.hairdesign, name='design-hairdesign'),
    path('news/', views.news, name='design-news'),
    path('contact/', views.contact, name='design-contact'),
]
