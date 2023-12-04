from django.utils.decorators import method_decorator
from django.views import View

from application.upload import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from utils import R


# 图片上传
@method_decorator(check_login, name='post')
class uploadImage(View):
    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用上传文件方法
        result = services.uploadImage(request)
        # 返回结果
        result = {
            'fileName': result['fileName'],
            'fileUrl': result['fileUrl'],
        }
        return R.ok(msg="上传成功", data=result)


# 富文本图片上传
@method_decorator(check_login, name='post')
class uploadEditImage(View):
    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用上传文件方法
        result = services.uploadImage(request)
        # 文件URL地址
        fileUrl = result['fileUrl']
        # 返回结果
        return R.ok(error=0, url=fileUrl)
