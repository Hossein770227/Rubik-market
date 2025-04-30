from django import forms

from website.models import Contact


class ContactForm(forms.ModelForm):
    class meta:
        model = Contact
        fields = ['email', 'message_subject', 'message']