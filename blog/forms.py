from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class contactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email Address')
    phone = forms.IntegerField(label='Phone Number')
    message = forms.CharField(widget=forms.Textarea, label='Message', max_length=1000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.form_action = 'contact'
        self.helper.layout = Layout(
            'name',
            'phone',
            'email',
            'message',
            Submit('submit', 'Submit')
        )

class commentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    comment = forms.CharField(label='Comment', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = 'postComment/'
        self.helper.form_class = 'size'
        self.helper.layout = Layout(
            'name',
            'comment',
            Submit('submit', 'Post')
        )
