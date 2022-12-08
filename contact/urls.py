from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('delivery/', views.delivery, name='delivery'),
    path('returns/', views.returns, name='returns'),
]
