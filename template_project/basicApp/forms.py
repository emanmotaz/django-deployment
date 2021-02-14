from django import forms
from django.contrib.auth.models import User
from basicApp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    """docstring for UserForm."""
    # To hash pass in view
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        # fields = ('__all__')
        fields = ('username','email','password')






class UserProfileInfoForm(forms.ModelForm):
    """docstring for UserProfileInfoForm."""
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
