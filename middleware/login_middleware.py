from django.shortcuts import redirect


# 检测是否已登录
def check_login(func):
    """定义装饰器"""

    # print("函数装饰器执行了")

    # 登录鉴权检测
    def wrapper(request, *args, **kwargs):
        # print("装饰器被调用了")
        # 在视图函数执行前做额外的操作

        # 登录检测
        # 自定义忽略URL数组
        ignoreURL = ['/login', '/captcha']
        # 用户ID
        user_id = request.session.get('user_id')
        if request.path not in ignoreURL and not user_id:
            # 重定向跳转
            return redirect('/login')

        # 一切正常，返回该返回的
        return func(request, *args, **kwargs)

    return wrapper
