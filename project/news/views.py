from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView  # ListView - Класс, который будет выводить список объектов из БД
from .models import Record
from .filters import RecordFilter


from .forms import RecordForm


class NewsList(ListView):                  # Класс, который наследуется от ListView
    model = Record                       # Указываем модель, объекты которой мы будем выводить
    ordering = ['-data']                    # Поле, которое будет использоваться для сортировки объектов
    template_name = 'news/news_home.html'  # Указываем имя шаблона. С инструкциями о том, как показать объекты юзеру
    context_object_name = 'record'        # Имя списка содержит все объекты. Его указать, для обр.к объектам в html
    paginate_by = 3                        # вот так мы можем указать количество записей на странице


class SearchList(ListView):
    model = Record
    ordering = ['-data']
    template_name = 'news/search.html'
    context_object_name = 'record'
    paginate_by = 3

    def get_filter(self):
        return RecordFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {**super().get_context_data(*args, **kwargs), 'filter': self.get_filter(), }

            # переменная фильтер будет использоваться в шаблоне


class NewsId(DetailView):
    model = Record
    template_name = 'news/news_id.html'
    context_object_name = 'record'


class NewsUpdataView(UpdateView):
    model = Record
    template_name = 'news/create.html'
    form_class = RecordForm


class NewsDeleteView(DeleteView):
    model = Record
    template_name = 'news/news_delete.html'
    success_url = '/news/'


def create(request):
    error = ''
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма заполнена не корректно'
    form = RecordForm()
    data = {'form': form, 'error': error}
    return render(request, 'news/create.html', data)