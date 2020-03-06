from django import forms as f

class NameForm(f.Form):
    your_name = f.CharField(label='Your Name', max_length=100)
