from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# هاد الكود بيحمي الصفحة الرئيسية (السيستم)، ممنوع تفتح بدون تسجيل دخول
@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # رابط شاشة الدخول اللي صممناها
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='/'), name='login'),
    
    # رابط السيستم (بيفتح بعد ما تسجل دخول صح)
    path('', home, name='home'),
]