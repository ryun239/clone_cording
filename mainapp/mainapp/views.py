from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.http.response import HttpResponse

from accountapp.models import User

# class HomeView(TemplateView):
#     template_name = 'home.html'
    

def index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('http://127.0.0.1:8000/post/')
    
        return render(request, "home.html")
    
