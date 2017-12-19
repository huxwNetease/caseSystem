from django.shortcuts import render, redirect

# Create your views here.
from . import models


def index(request):
    return render(request,'login.html')

def land(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
                    return render(request, 'index.html')
                else:
                    message = "密码不正确"
            except:
                message = "用户名不存在"
        return render(request, 'login.html', {"message": message})
    return render(request, 'index.html')