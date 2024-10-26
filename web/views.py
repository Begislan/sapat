from django.shortcuts import render
from database_admin.models import Person, Post


# Create your views here.
def index(request):
    persons = Person.objects.all()
    news_tree = Post.objects.all().order_by('-created_at')[:3]
    all_news = len(Post.objects.all())
    all_person = len(Person.objects.all())
    context = {
        'persons': persons,
        'news': news_tree,
        'all_news': all_news,
        'all_person': all_person,
    }
    return render(request, 'web/index.html', context)


def about(request):
    return render(request, 'web/about.html')


def about_info(request):
    return render(request, 'web/about_info.html')


def news(request):
    return render(request, 'web/news.html')

def news_detail(request):
    return render(request, 'web/news_detail.html')

def contact(request):
    return render(request, 'web/contact.html')