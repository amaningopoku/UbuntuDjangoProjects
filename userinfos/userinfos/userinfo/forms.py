from socket import fromshare
from django import forms
from.models import UserInfo

class UserInfoForm(forms.ModelForm):

    class meta:
        model = UserInfo
        exclude = ()