from django import forms

class FormularioDeContacto(forms.Form):
    #Este campo esta representado por un input del tipo text
    nombre = forms.CharField(max_length=40, min_length=3)

class FormularioDeQuejas(forms.Form):
    mail = forms.EmailField(max_length=20)
    cuerpo = forms.CharField(max_length=300)

class FormularioLogin(forms.Form):
    name = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    