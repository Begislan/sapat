from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем пользователя
            login(request, user)  # Автоматический вход после регистрации
            return redirect('admin_core')  # Перенаправляем на домашнюю страницу или другую страницу
    else:
        form = RegisterForm()

    return render(request, 'auth/register.html', {'form': form})



def custom_logout(request):
    logout(request)
    return redirect('/')