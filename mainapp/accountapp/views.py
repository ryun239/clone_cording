from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.generic import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.core.validators  import validate_email 
from django.core.exceptions  import ValidationError

from django.db import IntegrityError

from django.contrib.auth import login, logout, authenticate

from .models import User


class LoginView(View):
    def post(self, request):
        data = request.POST
        name = data['name']
        password = data['password']

        if name and password:
            user = authenticate(request, username = name, password = password) 
            if user:
                login(request, user)
                # return render(request,'postapp/post.html')
                return render(request,'post.html')
        else:
            return HttpResponse("not OK!!")


class LogoutView(View):
    def post(self, request):
        logout(request)
        return render(request,'home.html')


@method_decorator(csrf_exempt, name = "dispatch")
class BaseView(View):
    @staticmethod
    def response(data = {}, message = '', status = 200):
        result = {
            'data' : data,
            'message' : message,
        }
        return JsonResponse(result, status = status)

class UserCreateView(BaseView):
    @method_decorator(csrf_exempt)
    def get(self, request):
        return render(request, 'signin.html')


    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.POST

        print(data)
        # E-Mail
        email = data['emailid']
        try :
            validate_email(email)
        except ValidationError:
            return self.response(message = "missing email.", status = 400)

        # Password
        password = data['password']
        if not password:
            return self.response(message = 'missing passwd.', status = 400)

        # cpPassword
        cpassword = data['cpassword']
        if not cpassword:
            return self.response(message = 'missing passwd.', status = 400)

        if not password == cpassword:
            return self.response(message = 'password not same.', status = 400)

        # Name
        username = data['mem_name']
        print(username)
        if not username:
            return self.response(message = 'missing id', status = 400)

        dd = data['dd']
        mm = data['mm']
        yy = data['yyyy']
        if not (dd or mm or yy):
            return self.response(message = 'missing Birth Of Date', status = 400)
        else:
            birthofdate = yy + '-' + mm + '-' + dd
            print(birthofdate)
        
        gender = data['gender']
        if not gender:
            return self.response(message = 'missing Gender', status = 400)
        
        contactnum = data['contactnum']
        if not contactnum:
            return self.response(message = 'missing contactnum', status = 400)

        try :
            user = User.objects.create_user(
                
                email = email, 
                password = password,
                username = username, 
                Date_Of_Birth = birthofdate,
                Gender = gender,
                Phone_Num = contactnum
                )
        except IntegrityError:
            return self.response(message = "이미 존재하는 아이디입니다.", status = 400)

        return self.response({'user.email' : user.email})
