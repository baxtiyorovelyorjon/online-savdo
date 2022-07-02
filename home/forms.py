from django import forms

from home.models import Contact, NewsLatter


class NewsLatterForm(forms.ModelForm):
    class Meta:
        model = NewsLatter
        fields = ('email',)










  ## Contact form
class Form_contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name','email','phone','subject','message')
