from django.urls import re_path
from accounts import views
from django.contrib.auth import views as auth_views
from cuser.forms import AuthenticationForm
# from django.contrib.auth.views import LoginView


#TEMPLATES
app_name = 'accounts'
urlpatterns = [
    re_path(r'login/$', auth_views.LoginView.as_view(authentication_form=AuthenticationForm,
        template_name='accounts/login.html'), name='login'),
    re_path(r'logout$', auth_views.LogoutView.as_view(), name = 'logout'),
    re_path(r'signup/$', views.SignUp.as_view(), name = 'signup'),
    ]

    # re_path(r'^accounts/', include('django.contrib.auth.urls')),
