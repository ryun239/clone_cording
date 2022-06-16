from django.contrib import admin
from django.urls import path, include

from .views import HomeView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('account/', include('accountapp.urls')),
    path('post/', include('postapp.urls')),

]