from django.contrib.auth.forms import AuthenticationForm

from account.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['email', 'password']
