from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='about-club'),
	path('login/', views.login, name='login'),
	path('create_auction/', views.create_auction, name='create auction'),
    path('register/', views.register, name='register'),
    path('qr_inter/', views.qr_inter, name='qr_inter'),
    path('fill_auction/', views.fill_auction, name='fill_auction'),
]