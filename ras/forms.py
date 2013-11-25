from django import forms
from ras.models import ComplektSK
from django.forms.formsets import formset_factory



class ContactForm(forms.Form):

    error_css_class = 'error'
    required_css_class = 'required'

    Имя = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    Сообщение = forms.CharField(widget=forms.Textarea)


class BaseForm(forms.Form):
     class Meta:
        model = ComplektSK
        fields = ('name', 'price', 'weight')


