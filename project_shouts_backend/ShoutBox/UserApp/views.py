from UserApp.models import Comments
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
from UserApp.models import Users
from rest_framework.views import APIView
from UserApp.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import Users
import jwt, datetime
from .serializers import CommentSerializer, FriendSerializer, ShoutSerializer, UserSerializer
import json
from django.core.files.storage import FileSystemStorage
# # Create your views here.



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




class LoginView(APIView):
    def post(self, request):
        global result_token
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
        result_token = token
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        # token = request.COOKIES.get('jwt')
        token = result_token

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = Users.objects.filter(UserId=payload['id']).first()
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data,safe=False)

class LogoutView(APIView):

    def post(self, request):
        response = Response()
        print("in logout",response)
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


@csrf_exempt
def shoutsApi(request, UserId=0):
    if request.method == 'GET':
        if UserId != 0:
            shouts=Shouts.objects.filter(UserId=UserId)
            shouts_serializer = ShoutSerializer(shouts,many=True)
            return JsonResponse(shouts_serializer.data,safe=False)
        return JsonResponse("Shouts not found..",safe=False)

    elif request.method == 'POST':
        # print('in post')
        FileType = request.POST['FileType']
        post = request.POST
        # print('hi',FileType)
        # print(type(request.POST))
        # print(request.FILES)
        if FileType == 'image':
            # print('in fileType')
            fs = FileSystemStorage(location='D:/python_angular_project/Python_G5_ShoutBox/project_shouts_frontend/ShoutBox/src/assets/image')
            myfile = request.FILES['File']
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            uploaded_file_url = uploaded_file_url.replace("\\","/")
            uploaded_file_url = "../../../assets/image" + uploaded_file_url
            # print(uploaded_file_url)
        elif FileType == 'audio':
            # print('in fileType')
            fs = FileSystemStorage(location='D:/python_angular_project/Python_G5_ShoutBox/project_shouts_frontend/ShoutBox/src/assets/audio')
            myfile = request.FILES['File']
            filename = fs.save(myfile.name, myfile)
            # print(filename)
            uploaded_file_url = fs.url(filename)
            uploaded_file_url = uploaded_file_url.replace("\\","/")
            uploaded_file_url = "../../../assets/audio" + uploaded_file_url
            # print(uploaded_file_url)
        elif FileType == 'video':
            # print('in fileType')
            fs = FileSystemStorage(location='D:/python_angular_project/Python_G5_ShoutBox/project_shouts_frontend/ShoutBox/src/assets/video')
            myfile = request.FILES['File']
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            uploaded_file_url = uploaded_file_url.replace("\\","/")
            uploaded_file_url = "../../../assets/video" + uploaded_file_url
            # print(uploaded_file_url)
        result = request.POST.copy();
        result.__setitem__('File',uploaded_file_url)
        # print(result)
        result = json.dumps(result)
        result = json.loads(result)
        # print(type(result))
        shout_serializer=ShoutSerializer(data=result)
        # print('hi')
        if shout_serializer.is_valid():
                # print('done')
                shout_serializer.save()
                return JsonResponse("file Uploaded Successfully!!!", safe=False)
        else:
            # print('Not Working')
            return JsonResponse("Failed To Post Shout.", safe=False)


@csrf_exempt
def friendShoutsApi(request, UserId=0):
    if request.method == 'GET':
        if UserId != 0:
            friends=Friends.objects.filter(UserId=UserId) | Friends.objects.filter(FriendId=UserId)
            friends_serializers = FriendSerializer(friends,many=True)
            friend_list=friends_serializers.data
            friends_set=set()
            for i in friend_list:
                if i['StatusCode']==3:
                    friends_set.add(i['FriendId'])
            for i in friend_list:
                if i['StatusCode']==3:
                    friends_set.add(i['UserId'])

            shouts_list = list()
            for i in friends_set:
                shouts=Shouts.objects.filter(UserId=i).order_by('-ShoutsId')
                shouts_serializer = ShoutSerializer(shouts,many=True)
                shouts_list.append(shouts_serializer.data)

            # print(shouts_list)
            final_shouts_list=list()
            for i in shouts_list:
                for j in i:
                    final_shouts_list.append(j)
            final_friend_list_shouts = list()
            for i in final_shouts_list:
                friend_list_shouts= {
                        "ShoutsId":i['ShoutsId'],
                        "UserId":i['UserId'],
                        "DateCreated":i['DateCreated'],
                        "TextContent":i['TextContent'],
                        "File":i['File'],
                        "FileType":i['FileType'],
                        "IsDeleted":i['IsDeleted'],
                        "DateCreated":i['DateCreated'],
                        "FirstName":" ",
                        "LastName":" ",
                        "ProfilePicURL":" "
                        }
                final_friend_list_shouts.append(friend_list_shouts)

            friends_list = list()
            for i in final_shouts_list:
                friends=Users.objects.filter(UserId=i['UserId'])
                friends_serializer = UserSerializer(friends,many=True)
                friends_list.append(friends_serializer.data)

            final_friends_list=list()
            for i in friends_list:
                for j in i:
                    final_friends_list.append(j)
            # print(final_friends_list)
            for i in final_friend_list_shouts:
                for j in final_friends_list:
                    if i['UserId'] == j['UserId']:
                        i['FirstName'] = j['FirstName']
                        i['LastName'] = j['LastName']
                        i['ProfilePicURL'] = j['ProfilePicURL']

            # print(final_friend_list_shouts)
            final_max_shout_list = list()

            # print(type(UserId))
            # print(type(final_friend_list_shouts[0]['UserId'])

            for i in final_friend_list_shouts:
                     if str(i['UserId']) == UserId:
                         final_max_shout_list.append(i['ShoutsId'])

            final_max_shout_list.sort(reverse=True)
            # print(final_max_shout_list)

            final_shouts_list = list()

            for i in final_max_shout_list:
                for j in final_friend_list_shouts:
                    if i == j['ShoutsId']:
                        final_shouts_list.append(j)
                        final_friend_list_shouts.remove(j)
            for i in final_friend_list_shouts:
                final_shouts_list.append(i)

        return JsonResponse(final_shouts_list,safe=False)
    return JsonResponse("Shouts not found..",safe=False)


@csrf_exempt
def friendsListApi(request,UserId=0):
    if request.method == 'GET':
        if UserId != 0:
            friends=Friends.objects.filter(UserId=UserId) | Friends.objects.filter(FriendId=UserId)
            friends_serializers = FriendSerializer(friends,many=True)
            friend_list=friends_serializers.data
            friends_set=set()
            for i in friend_list:
                if i['StatusCode']==3:
                    friends_set.add(i['FriendId'])
            for i in friend_list:
                if i['StatusCode']==3:
                    friends_set.add(i['UserId'])

            friends_set.remove(int(UserId))

            friends_list = list()

            for i in friends_set:
                friends=Users.objects.filter(UserId=i)
                friends_serializer = UserSerializer(friends,many=True)
                friends_list.append(friends_serializer.data)

            final_friends_list=list()
            for i in friends_list:
                for j in i:
                    final_friends_list.append(j)

            return JsonResponse(final_friends_list,safe=False)
    return JsonResponse("Friends not found..",safe=False)

@csrf_exempt
def commentsApi(request,ShoutsId,UserId):
    if request.method == 'GET':
            if UserId != 0:
                # print('in GET hi')
                ShoutsId = ShoutsId.split(',')
                ShoutsId = list(ShoutsId)
                # print(type(ShoutsId))
                # print(ShoutsId)
                commentList = list()
                for i in ShoutsId:
                    comments=Comments.objects.filter(ShoutsId=i)
                    comments_serializer = CommentSerializer(comments,many=True)
                    commentList.append(comments_serializer.data)
                resultCommentList = list()
                # print('hello')
                # print(commentList)
                for i in commentList:
                    for j in i:
                        resultCommentList.append(j)
                # print(resultCommentList)


                users_set=set()
                users_list=list()

                for i in resultCommentList:
                    users_set.add(i['UserId'])

                for i in users_set:
                    user=Users.objects.filter(UserId=i)
                    users_serializer = UserSerializer(user,many=True)
                    users_list.append(users_serializer.data)

                final_users_list=list()
                for i in users_list:
                    for j in i:
                        final_users_list.append(j)

                all_comments = list()

                for i in resultCommentList:
                    comment= {
                        "FirstName":"",
                        "LastName":"",
                        "ProfilePicURL":"",
                        "ShoutsId":i['ShoutsId'],
                        "UserId":i['UserId'],
                        "CommentContent":i['CommentContent'],
                        "DateCreated":i['DateCreated'],
                        }
                    all_comments.append(comment)
                # print("in all comments")

                # print(all_comments)

                for i in all_comments:
                    for j in final_users_list:
                        if i['UserId'] == j['UserId']:
                            i['FirstName']=j['FirstName']
                            i['LastName']=j['LastName']
                            i['ProfilePicURL']=j['ProfilePicURL']
                # print("afer merging comments")
                # print(all_comments)
                return JsonResponse(all_comments,safe=False)


@csrf_exempt
def commentsUploadApi(request):
    if request.method == 'POST':
            comment = request.POST.copy();
            # print(comment)
            comment = json.dumps(comment)
            comment = json.loads(comment)
            comment_serializer= CommentSerializer(data=comment)
            if comment_serializer.is_valid():
                # print('done')
                comment_serializer.save()
                return JsonResponse("Comment Uploaded Successfully!!!", safe=False)
            return JsonResponse("Failed To Upload Comment.", safe=False)




@csrf_exempt
def friendRequestApi(request,UserId=0):
    if request.method == 'GET':
        try:
            if UserId != 0:
                friends=Friends.objects.filter(UserId=UserId) | Friends.objects.filter(FriendId=UserId)
                friends_serializers = FriendSerializer(friends,many=True)
                friend_list=friends_serializers.data
                print(friend_list)

                friends_set=set()
                for i in friend_list:
                    friends_set.add(i['UserId'])
                for i in friend_list:
                    friends_set.add(i['FriendId'])

                friends_set.remove(int(UserId))
                # print(friends_set)

                friends_list = list()
                for i in friends_set:
                    friends=Users.objects.filter(UserId=i)
                    friends_serializer = UserSerializer(friends,many=True)
                    friends_list.append(friends_serializer.data)

                final_friends_list=list()
                for i in friends_list:
                    for j in i:
                        final_friends_list.append(j)

                print(final_friends_list)

                friends_data_list=list()

                for i in final_friends_list:
                    friend_data ={
                        "FriendId" : i['UserId'],
                        "UserName" : i['UserName'],
                        "FirstName": i['FirstName'],
                        "LastName" : i['LastName'],
                        "Email" : i['Email'],
                        "MobileNo" : i['MobileNo'],
                        "Gender" : i['Gender'],
                        "DateOfBirth" : i['DateOfBirth'],
                        "ProfilePicURL" : i['ProfilePicURL'],
                        "DateCreated" : i['DateCreated'],
                        "StatusCode" : "",
                        "ActionUserId": ""
                    }
                    friends_data_list.append(friend_data)

                for i in friends_data_list:
                    for j in friend_list:
                        if (i['FriendId'] == j['UserId'] or i['FriendId'] == j['FriendId']):
                            i['StatusCode']=j['StatusCode']
                            i['ActionUserId']=j['ActionUserId']


                return JsonResponse(friends_data_list, safe=False)
        except:
            return JsonResponse("Record not found", safe=False)


@csrf_exempt
def friendRequestUpdateApi(request,UserId=0,FriendId=0,StatusCode=0):
    ((Friends.objects.filter(UserId=UserId) & Friends.objects.filter(FriendId=FriendId)) | (Friends.objects.filter(FriendId=UserId) & Friends.objects.filter(UserId=FriendId))).update(StatusCode=StatusCode)
    return JsonResponse("Updated Successfully!!!.", safe=False)

@csrf_exempt
def deleteShoutApi(request, ShoutId=0):
    if request.method=='DELETE':
        if ShoutId != 0:
            try:
                shout=Shouts.objects.get(ShoutsId=ShoutId)
                shout.delete()
                return JsonResponse("Shout Deleted Succeffully!!", safe=False)
            except:
                return JsonResponse("Shout Does Not Exists!!", safe=False)
    return JsonResponse("Failed To Delete Shout.", safe=False)

@csrf_exempt
def deleteCommentApi(request, CommentId=0):
    if request.method=='DELETE':
        if CommentId != 0:
            try:
                Comment=Comments.objects.get(CommentId=CommentId)
                Comment.delete()
                return JsonResponse("Comment Deleted Succeffully!!", safe=False)
            except:
                return JsonResponse("Comment Does Not Exists!!!", safe=False)
    return JsonResponse("Failed To Delete Comment.", safe=False)

