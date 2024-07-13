from django import forms
from . models import Contacto

class ContactoForms(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email_con', 'asunto', 'mensaje']
        labels = {
            'nombre': 'Nombre Completo',
            'email_con': 'Correo Electrónico',
            'asunto': 'Asunto',
            'mensaje': 'Mensaje'
        }

    def __init__(self, *args, **kwargs):
        super(ContactoForms, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escribe tu nombre'
        })
        self.fields['email_con'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escribe tu email'
        })
        self.fields['asunto'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escribe el asunto'
        })
        self.fields['mensaje'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escribe tu mensaje'
        })