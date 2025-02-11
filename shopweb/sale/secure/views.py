from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserLoginForm, ForgetForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Đăng nhập thành công')
                return redirect('w.home')
            else:
                messages.error(request, 'Đăng nhập thất bại')
                return redirect('w.login')
    else:
        form = UserLoginForm()
    return render(request, 'secure/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Đăng ký tài khoản thành công')
            return redirect('w.login')
    else:
        form = UserRegisterForm()
    return render(request, 'secure/register.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('w.home')

def forget_view(request):
    if request.method == 'POST':
        form = ForgetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, 'Email này không tồn tại.')
                return redirect('w.forget')
            new_pass = get_random_string(length=8)
            user.set_password(new_pass)
            user.save()
            subject = 'Khôi phục mật khẩu'
            message = f'Mật khẩu mới của bạn là: {new_pass}'
            from_email = 'nonameok2010@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Mật khẩu mới đã được gửi tới email của bạn.')
            return redirect('w.login')
    else:
        form = ForgetForm()
    return render(request, 'secure/forget.html', {'form': form})
