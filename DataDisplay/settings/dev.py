# -*- coding: utf-8 -*-
# 本地测试环境配置

from default import *
import socket

DEBUG = False

ALLOWED_HOSTS = ['*']

# ###################################################################
#                          DATABASES 配置
# ###################################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'data_analysis',
        'USER': 'Aaron',
        'PASSWORD': 'qwerty',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB',
        },
    },
    'master': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'data_analysis',
        'USER': 'Aaron',
        'PASSWORD': 'qwerty',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB',
        },
    },
}

# ###################################################################
#                          CACHE 配置
# ###################################################################
CACHES = {
    # 默认缓存
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 61200,
        'BINARY': True,
        'OPTIONS': {
            'ketama': True,
        }
    },
    # 文件缓存
    'file_cache': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
        'TIMEOUT': 61200,
        'OPTIONS': {
            'MAX_ENTRIES': 100000,
            'CULL_FREQUENCY': 3,
        }
    },
    # Redis 缓存
    "redis": {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        },
    },
}
