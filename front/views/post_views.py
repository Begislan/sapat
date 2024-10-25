from django.core.paginator import Paginator
from django.db.models import Q
from ..forms import PostForm, PostImageFormSet, PostImageForm
from datetime import datetime
from ..models import Post, PostImage, Person
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_core(request):
    current_user = request.user
    posts_all = Post.objects.all()
    persons = Person.objects.all()
    person = len(persons)
    posts = len(posts_all)
    context = {
        'posts_all': posts_all,
        'posts': posts,
        'current_user': current_user,
        'persons': person,
    }
    return render(request, 'adminka_post/admin_core.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_post(request):
    current_time = datetime.now()  # Текущая дата и время

    if request.method == 'POST':
        form = PostForm(request.POST)
        formset = PostImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())

        if form.is_valid() and formset.is_valid():
            post = form.save()  # Сохраняем объект Post

            # Сохраняем каждое изображение, связанное с постом
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    PostImage.objects.create(post=post, image=image)
            return redirect('all_posts')  # Перенаправляем на страницу успешного выполнения
    else:
        form = PostForm()
        formset = PostImageFormSet(queryset=PostImage.objects.none())

    context = {
        'form': form,
        'formset': formset,
        'current_time': current_time,
    }

    return render(request, 'adminka_post/admin_create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def success_create(request):
    return render(request, 'adminka_post/admin_create_success.html')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def all_posts(request):
    query = request.GET.get('q')  # Получаем запрос поиска
    posts = Post.objects.prefetch_related('images')  # Загружаем посты с изображениями

    # Фильтрация по дате и теме
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))

    paginator = Paginator(posts, 10)  # Создаем объект пагинатора с 10 постами на странице
    page_number = request.GET.get('page')  # Получаем номер страницы из запроса
    page_obj = paginator.get_page(page_number)  # Получаем объекты для отображения на текущей странице

    context = {
        'page_obj': page_obj,
        'query': query,  # Передаем запрос для отображения в форме поиска
    }
    return render(request, 'adminka_post/admin_all_posts.html', context)  # Обновите на свой шаблон


@login_required
@user_passes_test(lambda u: u.is_superuser)
def post_detail(request, id):
    post = Post.objects.prefetch_related('images').get(id=id)
    context = {
        'post': post,
    }
    return render(request, 'adminka_post/admin_detail.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)  # Получаем существующий пост
    current_time = datetime.now()  # Текущая дата и время

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # Передаем существующий объект post в форму

        if form.is_valid():
            form.save()  # Сохраняем только текстовые данные поста
            return redirect('post_detail', id=post.id)  # Перенаправляем на детальную страницу поста
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = PostForm(instance=post)  # Загружаем существующие данные поста

    context = {
        'form': form,
        'post': post,
        'current_time': current_time,  # Передаем текущую дату и время, если нужно для шаблона
    }

    return render(request, 'adminka_post/admin_edit.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)  # Получаем пост по ID
    if request.method == 'POST':  # Если запрос POST, удаляем пост
        post.delete()
        return redirect('all_posts')  # После удаления перенаправляем на список всех постов

    context = {
        'post': post,  # Передаем пост в шаблон для подтверждения удаления
    }
    return render(request, 'adminka_post/admin_delete_confirm.html', context)
