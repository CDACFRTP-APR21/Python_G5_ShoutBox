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
from UserApp.authetication import generate_access_token,JWTAuthetication
from .serializers import UserSerializer

# Create your views here.

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

@csrf_exempt
@api_view(['GET', 'POST'])
def loginApi(request):
        data=JSONParser().parse(request)
        email = data['Email']
        password = data['Password']
    
        user = Users.objects.get(Email=email,Password=password)
        response = Response()
        
        userId = user.UserId
        token = generate_access_token(userId)
        print(token)
        response.set_cookie(key='jwt',value=token,httponly=True)
       
        response.data = {
         'jwt':token
        }

        print(response.data['jwt'])
        return response

    
    # else:
    #     raise exceptions.AutheticationFailed("user not found")


class AutheticatedUser(APIView):
    authication_classes = [JWTAuthetication]
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self,request):
        serializer = UserSerializer(request.user)
        
        return Response({
            'data':serializer.data
        })

   
