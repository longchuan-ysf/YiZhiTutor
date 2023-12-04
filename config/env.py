# ======================= 应用配置 ==========================

# 开启DEBUG调试
DEBUG = False

# ======================= 数据库配置 ==========================

# 数据库 ENGINE ，默认演示使用 sqlite3 数据库，正式环境建议使用 mysql 数据库
# sqlite3 设置
# DATABASE_ENGINE = "django.db.backends.sqlite3"
# DATABASE_NAME = os.path.join(BASE_DIR, "db.sqlite3")

# 使用mysql时，改为此配置
DATABASE_ENGINE = "django.db.backends.mysql"
# 数据库库名
DATABASE_NAME = 'djangoadmin'  # mysql 时使用
# 数据库地址 改为自己数据库地址
DATABASE_HOST = "127.0.0.1"
# 数据库端口
DATABASE_PORT = 3306
# 数据库用户名
DATABASE_USER = "root"
# 数据库密码
DATABASE_PASSWORD = "008194"
# 数据表前缀
TABLE_PREFIX = "django_"

# 全局变量
# 图片地址
IMAGE_URL = "http://mylocaluploads.com"
# 附件存储目录
ATTACHMENT_PATH = "E:/3school/GraduationDesign/software/uploads"
IMAGE_PATH = '{}/images'.format(ATTACHMENT_PATH)
TEMP_PATH = '{}/temp'.format(ATTACHMENT_PATH)
