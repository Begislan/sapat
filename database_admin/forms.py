from django import forms
from .models import Post, PostImage, Person
from django.forms import modelformset_factory

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at']  # Поля для поста

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']  # Поле для загрузки изображения


PostImageFormSet = modelformset_factory(PostImage, form=PostImageForm, extra=10)  # Можно загрузить до 10 изображений

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'




