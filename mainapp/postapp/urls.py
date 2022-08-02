from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import PostView, UserTweet

app_name = 'postapp'
urlpatterns = [
    path('', PostView.as_view(), name='post'),
    path('tweet/', UserTweet.as_view(), name='tweet'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)