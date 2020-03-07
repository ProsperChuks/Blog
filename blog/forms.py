from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)

class contactForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email Address')
    phone = forms.IntegerField(label='Phone Number')
    messgae = forms.CharField(widget=forms.Textarea, label='Message')
