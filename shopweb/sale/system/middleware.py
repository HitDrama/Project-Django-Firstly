from django.conf import settings
from django.shortcuts import redirect, render
from .models import Config

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # Get the current view function and its app name
        current_path = request.path
        #check login
        if current_path.startswith('/system/') and not request.user.is_authenticated:

            return redirect('/secure/login')
        #check role
        if current_path.startswith('/system/') and not request.user.is_superuser:
            return redirect('/')
        
        response = self.get_response(request)
        return response
    
class BaotriMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        current_path = request.path
        try:
            maintenance = Config.objects.first()
            if maintenance and maintenance.active and not current_path.startswith('/system/') and not current_path.startswith('/secure/login') and not current_path.startswith('/secure/logout'):
                return render(request,'pages/baotri.html',{
                    'message':maintenance.note
                })
        except maintenance.DoesNotExist:
            pass
        response = self.get_response(request)
        return response