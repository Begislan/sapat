from django.urls import path
from .views import (index, about, about_info, news, news_detail, contact)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path("about-info/", about_info, name='about_info'),
    path("news/", news, name='news'),
    path("newsd/", news_detail, name='news_detail'),
    path('contact/', contact, name='contact'),
]