from django.contrib import admin
from django.urls import path, include  # метод include, делегирует обращение urls нашего приложения

# список адресов для отслеживания
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('new_portal.urls')),  # отслеживание главной страницы
    path('news/', include('news.urls')),
]
