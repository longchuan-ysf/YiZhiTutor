import json

from django.core import serializers
from django.core.management import BaseCommand

# 自定义命令管理生成JSON初始化文件
from application.level.models import Level


class Command(BaseCommand):
    help = '每日凌晨对当天数据库进行更新'  # command功能作用简介

    # 添加参数
    def add_arguments(self, parser):  # 用来接收可选参数的( 如果没有参数该方法可以不写 )
        # parser.add_argument('offset', type=int, help='天数转移量')

        parser.add_argument("--model", nargs="*", type=str, help="初始化生成的表名")

    # def generate_users(self):
    #     self.serializer_data(UsersInitSerializer, Users.objects.all())

    # 执行句柄，主处理程序
    def handle(self, *args, **options):
        # 数据表对应的模型名称
        model = options['model']
        # 模块字典
        model_dict = {

        }
        with open("file.json", "w") as out:
            data = serializers.serialize("json", Level.objects.all())
            # data = json.loads(json.dumps(data, ensure_ascii=False))
            # json.dump(data, out, indent=2, ensure_ascii=False)
            # json.dumps(data, ensure_ascii=False)

            data = json.loads(data)
            out.write(data)

        # serializer = serializer(query_set, many=True)
        #
        # with open(os.path.join(BASE_DIR, f'init_{query_set.model._meta.model_name}.json'), 'w') as f:
        #     json.dump(data, f, indent=4, ensure_ascii=False)
