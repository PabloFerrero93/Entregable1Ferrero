from django import forms

class HermanoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    nacimiento = forms.DateField()
