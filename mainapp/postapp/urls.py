from django.urls import path, include
from .views import PostView

app_name = 'postapp'
urlpatterns = [
    path('', PostView.as_view(), name='post'),
]