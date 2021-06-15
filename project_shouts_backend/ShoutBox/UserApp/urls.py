from django.conf.urls import url
from django.urls.resolvers import URLPattern
from UserApp import views

urlpatterns=[
    url(r'^user/$',views.userApi),
    url('^user/([0-9]+)$',views.userApi)
]