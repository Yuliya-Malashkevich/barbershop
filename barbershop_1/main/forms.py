from django import forms

class userForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=20)
    email = forms.EmailField(min_length=3, max_length=20)
    phone = forms.CharField(min_length=3, max_length=20)
    required_css_class = "field"
