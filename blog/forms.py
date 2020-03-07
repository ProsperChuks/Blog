from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)

class contactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    phone = forms.IntegerField(label='Phone Number')
    message = forms.CharField(widget=forms.Textarea, label='Message', max_length=1000)
