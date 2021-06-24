from UserApp.models import Comments
from UserApp.models import Friends
from UserApp.models import Shouts
from rest_framework import serializers
from UserApp.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('UserId',
                    'UserName',
                    'FirstName',
                    'LastName',
                    'Email',
                    'MobileNo',
                    'Password',
                    'Gender',
                    'DateOfBirth',
                    'ProfilePicURL',
                    'DateCreated',
                    'IsActive',
                    )

class ShoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shouts
        fields = ('ShoutsId',
                    'UserId',
                    'DateCreated',
                    'TextContent',
                    'File',
                    'IsDeleted',
                    'FileType'
                    )

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('UserId',
                    'FriendId',
                    'StatusCode',
                    'ActionUserId',
                    'DateCreated'
                    )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('CommentId',
                    'ShoutsId',
                    'UserId',
                    'CommentContent',
                    'DateCreated'
                    )