from .models import Record
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class RecordForm(ModelForm):
    class Meta:  # в нем укажем характеристики
        model = Record  # модель с которой будем работать
        # создадим список полей
        fields = ['title', 'full_text', 'data', 'category']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            'data': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
            'full_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст статьи'}),
            'category': TextInput(attrs={'class': 'form-control', 'placeholder': 'Категория'}),

        }

#
# class SearchForm(ModelForm):
#     class Meta:  # в нем укажем характеристики
#         model = Record  # модель с которой будем работать
#         # создадим список полей
#         fields = ['title', 'category', 'data']
#
#         widgets = {
#             'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
#             'data': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
#             'category': Textarea(attrs={'class': 'form-control', 'placeholder': 'Категория'}),
#         }