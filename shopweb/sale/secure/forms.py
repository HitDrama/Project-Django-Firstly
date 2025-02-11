from .models import CustomUser,User
from django import forms
from django.contrib.auth.forms import UserCreationForm

#form user
class UserRegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your username'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username') 
        if not username.isalnum():
            raise forms.ValidationError("Username chỉ chứa ký tự với số")
        if len(username) < 5 or len(username) >32:
            raise forms.ValidationError("Username phải bao gó 5-32 ký tự")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        if len(password1) < 8:
            raise forms.ValidationError("Password phải bao gó 8 ký tự")
        return password1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password2')
        
class UserLoginForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your username'}))

class Meta:
    model = CustomUser
    fields = ['username', 'password1']

class ForgetForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email'}))

class Meta:
    model = CustomUser
    fields = ['email']