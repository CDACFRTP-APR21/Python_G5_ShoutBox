from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from UserApp.models import Users
from UserApp.serializers import UserSerializer


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