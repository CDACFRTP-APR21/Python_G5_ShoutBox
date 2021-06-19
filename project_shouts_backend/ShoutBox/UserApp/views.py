from UserApp.models import Friends
from UserApp.models import Shouts
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated, OR
from UserApp.models import Users
from rest_framework.views import APIView
from UserApp.serializers import UserSerializer
from rest_framework.response import Response
from UserApp.authetication import generate_access_token,JWTAuthetication
from .serializers import FriendSerializer, ShoutSerializer, UserSerializer

# Create your views here.



@csrf_exempt
def userApi(request, UserId=0):
    if request.method == 'GET':
        if UserId != 0:
            user=Users.objects.filter(UserId=UserId)
            users_serializer = UserSerializer(user,many=True)
        else:
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
    
    elif request.method == 'PUT':
        user_data=JSONParser().parse(request)
        user = Users.objects.get(UserId=UserId)
        user_serializer= UserSerializer(user,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!!!", safe=False)
        return JsonResponse("Failed To Update.", safe=False)

    elif request.method=='DELETE':
        user=Users.objects.get(UserId=UserId)
        user.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)



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

   
@csrf_exempt
def shoutsApi(request, UserId=0):
    if request.method == 'GET':
        if UserId != 0:
            shouts=Shouts.objects.filter(UserId=UserId)
            shouts_serializer = ShoutSerializer(shouts,many=True)
        return JsonResponse(shouts_serializer.data,safe=False)
    return JsonResponse("Shouts not found..",safe=False)


@csrf_exempt
def friendShoutsApi(request, UserId=0):
    if request.method == 'GET':
        if UserId != 0:
            friends=Friends.objects.filter(UserId=UserId) | Friends.objects.filter(FriendId=UserId)
            friends_serializers = FriendSerializer(friends,many=True)
            friend_list=friends_serializers.data
            friends_set=set()
            for i in friend_list:
                friends_set.add(i['FriendId'])
            for i in friend_list:
                friends_set.add(i['UserId'])
            
            shouts_list = list()

            for i in friends_set:
                shouts=Shouts.objects.filter(UserId=i)
                shouts_serializer = ShoutSerializer(shouts,many=True)
                shouts_list.append(shouts_serializer.data)

        return JsonResponse(shouts_list,safe=False)
    return JsonResponse("Shouts not found..",safe=False)