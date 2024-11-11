from database_admin.models import Files, Contact
from django.shortcuts import render


def view_contacts(request):
    contacts_feedback = Contact.objects.all()
    return render(request, "adminka_contact_feedback/feedback.html", {"feedbacks": contacts_feedback})