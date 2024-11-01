from django.shortcuts import render, redirect
from database_admin.models import Person, Post
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from database_admin.forms import ContactForm


# Create your views here.
def index(request):
    # Получаем последние 3 поста
    latest_posts = Post.objects.prefetch_related('images').order_by('-created_at')[:3]

    # Готовим посты с первыми изображениями
    posts_with_images = []
    for post in latest_posts:
        first_image = post.images.first()  # Получаем первое связанное изображение
        posts_with_images.append({
            'post': post,
            'image': first_image.image.url if first_image else None
        })

    context = {
        'posts_with_images': posts_with_images
    }
    return render(request, 'web/index.html', context)


def about(request):
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'web/about.html', context)

def about_detail(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    context = {
        'person': person
    }
    return render(request, 'web/about_detail.html', context)


def about_info(request):
    return render(request, 'web/about_info.html')


def news(request):
    query = request.GET.get('search', '')  # Получаем поисковый запрос

    latest_posts = Post.objects.prefetch_related('images').order_by('-created_at')

    posts_with_images = []
    for post in latest_posts:
        first_image = post.images.first()  # Получаем первое связанное изображение
        posts_with_images.append({
            'post': post,
            'image': first_image.image.url if first_image else None
        })



    posts = Post.objects.order_by('-created_at')
    if query:
        posts = posts.filter(title__icontains=query)
    paginator = Paginator(posts, 4)  # Пагинация: 4 поста на страницу

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts_with_images': posts_with_images,
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'web/news.html', context)

def news_detail(request, post_id):
    # Получаем последние 3 поста
    latest_posts = Post.objects.prefetch_related('images').order_by('-created_at')[:3]

    posts_with_images = []
    for post in latest_posts:
        first_image = post.images.first()  # Получаем первое связанное изображение
        posts_with_images.append({
            'post': post,
            'image': first_image.image.url if first_image else None
        })

    # Получаем пост по его ID и его связанные изображения
    post = get_object_or_404(Post, id=post_id)
    images = post.images.all()  # Все изображения, связанные с постом

    context = {
        'post': post,
        'images': images,
        'related_posts': posts_with_images
    }
    print(post)
    return render(request, 'web/news_detail.html',context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем сообщение в базе данных
            return redirect('contact_success')  # Перенаправляем на страницу успешной отправки
    else:
        form = ContactForm()
    return render(request, 'web/contact.html', {'form':form})

def contact_success(request):
    return render(request, 'web/contact_success.html')