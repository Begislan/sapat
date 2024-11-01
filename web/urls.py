from django.urls import path
from .views import (index, about, about_info, news, news_detail, contact, contact_success, about_detail)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path("about-info/", about_info, name='about_info'),
    path("news/", news, name='news'),
    path("news/<int:post_id>", news_detail, name='news_detail'),
    path('contact/', contact, name='contact'),
    path("contact-success/", contact_success, name='contact_success'),
    path('about-detail/<int:person_id>', about_detail, name='about_detail'),
]