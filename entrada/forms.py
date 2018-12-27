from django import forms

from .models import Registrados

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrados
        fields = ["nombre","email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not "com" in extension:
             raise forms.ValidationError("Se requiere un email que  termine con .com") 
        return email    

class ContacForm(forms.Form):
    nombre = forms.CharField(required=False)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)