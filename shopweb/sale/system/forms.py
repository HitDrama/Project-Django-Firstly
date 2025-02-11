from django import forms
from .models import Category, Product,Config
from django.contrib.auth.forms import UserCreationForm
from secure.models import CustomUser
from ckeditor.widgets import CKEditorWidget

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'keywords', 'desc', 'slug', 'parent', 'image', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your title',
            }),
            'keywords': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your keyword',
            }),
            'desc': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your description',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your slug',
            }),
            'parent': forms.Select(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'status': forms.TextInput(attrs={
                'type': 'number',
                'class': 'form-control',
            }),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'keyword', 'decription', 'price', 'category', 'image', 'status']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'keyword': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your keywords',
            }),
            # 'decription': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Enter your description',
            # }),
            'decription': CKEditorWidget(),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your price',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'status': forms.TextInput(attrs={
                'type': 'number',
                'class': 'form-number',         
            }),
        }

#Form user 
class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email'}))
    option = [
        ('True', 'Admin'),
        ('False', 'User'),
    ]
    is_superuser = forms.ChoiceField(widget=forms.RadioSelect, choices=option, initial='False')
    
    optionac = [
        ('True', 'Active'),
        ('False', 'Hide'),
    ]
    is_active = forms.ChoiceField(widget=forms.RadioSelect, choices=optionac, initial='True')
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter your phone'}))
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'phone', 'is_superuser', 'is_active', 'image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password2')

    # validate
    def clean_username(self):
        ten = self.cleaned_data.get('username') 
        if not ten.isalnum():
            raise forms.ValidationError("Username chỉ chứa ký tự với số")
        if len(ten) < 5 or len(ten) >32:
            raise forms.ValidationError("Username phải bao gồm 5-32 ký tự")
        if not self.instance.id:
            if CustomUser.objects.filter(username=ten).exists():
                raise forms.ValidationError("Username đã tồn tại.")
        return ten
    
    def clean_password1(self):
        matkhau = self.cleaned_data.get('password1')
        
        if len(matkhau) < 8:
            raise forms.ValidationError("Password phải bao gồm 8 ký tự")
        return matkhau
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not self.instance.id:
            if CustomUser.objects.filter(email=email).exists():
                raise forms.ValidationError("Email đã được đăng ký.")
        return email
    
class ConfigForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your name'}))
    keyword = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your keyword'}))
    decription = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your decription'}))
    domain = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your domain'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your email'}))
    past_mail = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your pass mail'}))
    host_mail = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your host mail'}))
    option=[
        (True,'Bật Bảo Trì'),
        (False,'Tắt Bảo Trì'),
    ]
    active=forms.ChoiceField(choices=option,initial=True,widget=forms.RadioSelect)
    note = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your note'}))
    image=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}),required=False)

    class Meta:
        model = Config
        fields = ['name', 'keyword', 'decription','domain','email','past_mail','host_mail','active','note','image']