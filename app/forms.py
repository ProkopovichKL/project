from django import forms
from app.models import PotencialClient

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length = 2,
        max_length = 60,
        widget=forms.TextInput(attrs = {'placeholder':'Your name', 'class':'form-control'}))
       
    email = forms.EmailField(
        widget=forms.EmailInput(attrs = {'placeholder':'E-mail', 'class':'form-control'}))

    message = forms.CharField(
        min_length = 10,
        max_length = 600,
        widget=forms.Textarea(attrs = {'placeholder':'Write your message', 'cols':'30', 'rows':'10', 'class':'form-control'}))

class ClientForm(forms.ModelForm):
    class Meta:
        model = PotencialClient
        fields = "__all__"
