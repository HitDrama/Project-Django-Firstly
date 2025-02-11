from django.urls import path
from secure import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='w.login'),
    path('register/', views.register_view, name='w.register'),
    path('logout/', views.logout_view, name='w.logout'),
    path('forget/', views.forget_view, name='w.forget'),
]
