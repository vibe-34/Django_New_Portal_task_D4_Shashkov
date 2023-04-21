from django.contrib import admin
from django.urls import path, include  # метод include, делегирует обращение urls нашего приложения

# from django.conf import settings
# from django.conf.urls.static import static

# список адресов для отслеживания
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('new_portal.urls')),  # отслеживание главной страницы
    path('news/', include('news.urls')),
]  #  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
