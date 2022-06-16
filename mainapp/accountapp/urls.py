from django.urls import path, include
from .views import UserCreateView, LoginView, LogoutView



app_name = "accountapp"
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='signup'),
]