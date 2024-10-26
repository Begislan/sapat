from django.shortcuts import render, get_object_or_404, redirect
from ..models import Post, PostImage, Person
from ..forms import PersonForm
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda u: u.is_superuser)
def persons(request):
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'adminka_person/persons.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)  # Поддержка файлов для изображения
        if form.is_valid():
            form.save()
            return redirect('persons')  # Перенаправление на список сотрудников после создания
    else:
        form = PersonForm()

    context = {
        'form': form
    }
    return render(request, 'adminka_person/person_create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def person_detail(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    context = {
        'person': person
    }
    return render(request, 'adminka_person/person_detail.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)

    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_detail', person_id=person.id)
    else:
        form = PersonForm(instance=person)

    context = {
        'form': form,
        'person': person
    }
    return render(request, 'adminka_person/person_edit.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)

    if request.method == 'POST':
        person.delete()
        return redirect('persons')  # Перенаправляем на список сотрудников после удаления

    context = {
        'person': person
    }
    return render(request, 'adminka_person/person_confirm_delete.html', context)
