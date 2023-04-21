import django_filters
from .models import Record, Category
from django import forms


class RecordFilter(django_filters.FilterSet):

    data = django_filters.DateRangeFilter(widget=forms.TextInput(attrs={'type': 'date'}), label='Поиск по дате',)
    title = django_filters.CharFilter(lookup_expr='icontains',)

    class Meta:
        model = Record
        fields = ['category', ]




# category = django_filters.CharFilter(
#         field_name='category__title',
#         label='Категория',
#         lookup_expr='icontains',
#     )






# работает по полному названию и категории + вместе
# from django_filters import FilterSet
# from .models import Record
# from django import forms
# class RecordFilter(FilterSet):
#     class Meta:
#         model = Record
#         fields = [
#             'title',
#             'category',
#             'data',
#         ]

