from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre',max_length=50, required=True)
    email = forms.EmailField(label='Email',required=True)
    contenido = forms.CharField(label='Contenido',widget=forms.Textarea,max_length=100,required=True)
    