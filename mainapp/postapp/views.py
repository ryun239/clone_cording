from django.shortcuts import render
from django.views.generic import View
from .models import Tweet


class PostView(View):
    def get(self, request):
        return render(request, 'index.html')
    

class UserTweet(View):
    def post(self, request):
        print(request)

        # data = request.POST
        # db = Tweet() 

        # db.Text = data['feed']
        # db.Img  = data['img']

        # # db.save()
        # return render(request, 'index.html')

