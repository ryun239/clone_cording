from django.shortcuts import render
from django.views.generic import View
from .models import Tweet

from django.conf import settings

from accountapp.models import User

class PostView(View):
    def get(self, request):
        print(request.user)
        if request.user.is_authenticated:
            u = User.objects.filter(username=request.user).values()
            print("in")
            print(u[0]['Profile'])
            print(settings.MEDIA_ROOT)
            print(settings.MEDIA_URL)
            
        return render(request, 'index.html', {'img': u[0]['Profile']})
    

class UserTweet(View):
    def post(self, request):
        print(request)

        # data = request.POST
        # db = Tweet() 

        # db.Text = data['feed']
        # db.Img  = data['img']

        # # db.save()
        # return render(request, 'index.html')

