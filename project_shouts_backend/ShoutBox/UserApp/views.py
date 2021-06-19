from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from UserApp.models import Users
from rest_framework.views import APIView
from UserApp.serializers import UserSerializer
from rest_framework.response import Response
# from UserApp.authetication import generate_access_token,JWTAuthetication
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import Users
import jwt, datetime



# # Create your views here.

@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UserSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)
    
    elif request.method == 'POST':
        user_data=JSONParser().parse(request)
        user_serializer= UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Registered Successfully!!!", safe=False)
        return JsonResponse("Failed To Register.", safe=False)


class LoginView(APIView):
    def post(self, request):
        email = request.data['Email']
        password = request.data['Password']

        user = Users.objects.filter(Email=email,Password=password).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        payload = {
            'id': user.UserId,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = Users.objects.filter(UserId=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response