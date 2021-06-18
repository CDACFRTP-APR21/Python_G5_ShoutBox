from django.conf.urls import url
from django.urls.resolvers import URLPattern
from UserApp import views
from .views import AutheticatedUser

urlpatterns=[
    url(r'^user/$',views.userApi),
    url(r'^user/([0-9]+)$',views.userApi),
    url(r'^login',views.loginApi),
    url(r'^users',AutheticatedUser.as_view())
]