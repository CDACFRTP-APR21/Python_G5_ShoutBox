from django.conf.urls import url
from django.urls.resolvers import URLPattern
from UserApp import views
from .views import UserView
from django.urls import path
from .views import LoginView, UserView, LogoutView
from .views import shoutsApi

urlpatterns=[
    url(r'^user/$',views.userApi),
    url(r'^user/([0-9]+)$',views.userApi),
    url(r'^shouts/([0-9]+)$',views.shoutsApi),
    url(r'^friendShouts/([0-9]+)$',views.friendShoutsApi),
    url(r'^friendsList/([0-9]+)$',views.friendsListApi),
    url(r'^comments/([0-9,]+)/([0-9]+)$',views.commentsApi),
    url(r'^commentsUpload/$',views.commentsUploadApi),
    path('login', LoginView.as_view()),
    path('users', UserView.as_view()),
    path('logout', LogoutView.as_view())
]