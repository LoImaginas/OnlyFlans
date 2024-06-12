from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['email_del_cliente', 'nombre_del_cliente', 'mensaje']