from django.urls import re_path
from campaigns import views

app_name = 'campaigns'
urlpatterns = [
    re_path(r'chome/$', views.ClientHome.as_view(), name= 'clienthome'),
]
