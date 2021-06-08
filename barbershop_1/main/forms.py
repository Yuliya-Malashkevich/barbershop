from .models import Reviews  # отзывы
from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput  #для создания формы отзывов

class userForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=20)
    email = forms.EmailField(min_length=3, max_length=20)
    phone = forms.CharField(min_length=3, max_length=20)
    required_css_class = "field"

class ReviewsForm(ModelForm):  #для создания формы отзывов
    class Meta:
        model = Reviews
        fields = ['name', 'review_text', 'date']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "review_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст отзыва'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
        }
