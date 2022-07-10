import os



# 项目的工作目录  比如我们要  指定静态文件 或者 模板 的时候就会使用 BASE_DIR进行路径的拼接
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 密钥
SECRET_KEY = '54ojz@9q4v#_8-!b+)9_1!-(5n@7&&2^uewutr_x7zy!*mean$'

# True:调试阶段     会显示报错
# False:生产阶段    不会显示报错      部署后一定要开为False
DEBUG = True

# 允许访问的主机   默认只有127.0.0.1   可添加网页链接，或者可访问的域名、或者*（表示所有域名都可添加），搭配着debug进行使用。
ALLOWED_HOSTS = []

# 子应用注册列表   一个子应用就代表前端的一个功能
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',         # 默认情况下，Django将Session存入数据库中
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sales',                           # 将子应用sales注册到项目中（老式写法）
    'common.apps.CommonConfig',        # 将子应用common注册到项目中（新）
    'hello',
]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路由配置
ROOT_URLCONF = 'untitled.urls'

# 模板  使用模板时需要在DIRS里进行一个路径的拼接，在我们的Django启动之后，如果有用到这个模板的话，就会在我们拼接的路径中进行查找，如果没有就返回404。
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 启动服务的时候需要用到的WSGI协议
WSGI_APPLICATION = 'untitled.wsgi.application'

# 数据库配置，其中的sqlite3可修改成mysql，也就是修改数据库。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 密码有效性认别
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 时区，语言等
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# 静态文件访问路径 (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# 建立(/添加)静态文件的查找目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static') # 把新建的static文件夹加到静态文件的查找目录

]