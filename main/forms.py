from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(help_text='A valid email address, please.')
    subject = forms.CharField(max_length=100, help_text='100 characters max.')
    message = forms.CharField(max_length=500, help_text='500 characters max.')
