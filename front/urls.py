from django.urls import path
from .views import (admin_core, create_post, success_create,
                    all_posts, post_detail, edit_post,
                    delete_post, persons, person_detail,
                    edit_person, delete_person, create_person
                    )

urlpatterns = [
    path('', admin_core, name='admin_core'),
    path('admin_create_post/', create_post, name='create_post'),
    path('admin_create_success/', success_create, name='create_success'),
    path('all_posts/', all_posts, name='all_posts'),
    path('post/<int:id>', post_detail, name='post_detail'),
    path('post/<int:id>/edit/', edit_post, name='edit_post'),
    path('post/<int:id>/delete/', delete_post, name='post_delete'),

    # Person

    path('persons/', persons, name='persons'),

    path('persons/create/', create_person, name='create_person'),
    path('persons/<int:person_id>/', person_detail, name='person_detail'),
    path('persons/<int:person_id>/edit/', edit_person, name='edit_person'),
    path('persons/<int:person_id>/delete/', delete_person, name='delete_person'),

]
