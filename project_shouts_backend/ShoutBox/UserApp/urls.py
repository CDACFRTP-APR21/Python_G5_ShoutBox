from django.conf.urls import url
from django.urls.resolvers import URLPattern
from UserApp import views
from .views import AutheticatedUser, shoutsApi

urlpatterns=[
    url(r'^user/$',views.userApi),
    url(r'^user/([0-9]+)$',views.userApi),
    url(r'^login',views.loginApi),
    url(r'^users',AutheticatedUser.as_view()),
    url(r'^shouts/([0-9]+)$',views.shoutsApi),
    url(r'^friendShouts/([0-9]+)$',views.friendShoutsApi),
    url(r'^friendsList/([0-9]+)$',views.friendsListApi),
    url(r'^comments/([0-9]+)/([0-9]+)$',views.commentsApi),
    url(r'^commentsUpload/([0-9]+)/([0-9]+)$',views.commentsUploadApi)
    
]