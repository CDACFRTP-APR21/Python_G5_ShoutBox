from django.conf.urls import url
from django.urls.resolvers import URLPattern
from UserApp import views
from .views import UserView
from django.urls import path
from .views import LoginView, UserView, LogoutView

urlpatterns = [
     url(r'^user/$',views.userApi),
     url(r'^user/([0-9]+)$',views.userApi),
    path('login', LoginView.as_view()),
    path('users', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]