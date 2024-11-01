from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)  # Связь с постом
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'Image for {self.post.title}'


    class Meta:
        ordering = ['post']
        verbose_name = 'Картина'
        verbose_name_plural = "Каритины"


class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    first_name = models.CharField(max_length=200, verbose_name='Фамилия')
    last_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Отечество')
    speciality = models.CharField(max_length=200, verbose_name='Должность')
    spec = models.CharField(max_length=255, verbose_name="Степень")
    faculty = models.CharField(max_length=200, null=True, blank=True, verbose_name='Институт, коллдеж')
    kafedra = models.CharField(max_length=200, null=True, blank=True, verbose_name='Кафедра, цикл')
    img = models.FileField(upload_to='images/', verbose_name='Изображение сотрудника', null=True, blank=True)
    addres = models.CharField(max_length=255, verbose_name='Адрес')
    tel = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.first_name})"

    class Meta:
        ordering = ['name']
        verbose_name = 'Сотрудники'
        verbose_name_plural = "Сотрудники"

class Files(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Файл'
        verbose_name_plural = 'Файлы'


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name