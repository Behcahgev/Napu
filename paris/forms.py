from django import forms
from .models import BetRoom

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = BetRoom
        fields = ('name','public',)
