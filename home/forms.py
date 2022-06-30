from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'text')
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': '*نام...'}),
            "email": forms.TextInput(attrs={'class': 'form-control', 'placeholder': '*ایمیل...'}),
            "text": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیام شما...', 'clos': '5', 'row': '5', 'style': 'height: 145px'})
        }
