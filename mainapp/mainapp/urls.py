from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from .views import index

app_name = "mainapp"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('account/', include('accountapp.urls')),
    path('post/', include('postapp.urls'), name='post'),
]