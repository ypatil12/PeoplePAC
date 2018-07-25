from django.contrib.auth import get_user_model
from django.core import validators
from cuser.forms import UserCreationForm
from django.conf import settings

class UserSignUpForm(UserCreationForm):

    class Meta():
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['email'].label = "Email Address"
