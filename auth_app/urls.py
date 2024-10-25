from django.urls import path
from django.contrib.auth import views as auth_views
from .views import custom_logout, register  # Ваши собственные представления

urlpatterns = [
    # Стандартные маршруты для входа и выхода
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),

    # Регистрация
    path('register/', register, name='register'),
]
