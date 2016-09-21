# -*- coding: utf-8 -*-
import hashlib
import random
import string
import time
import uuid


def generate_random_str(length=8):
    """
    生成随机字符串.默认是8位
    :param length: 长度设置.
    :return:    指定长度的string
    """
    a = list(string.printable)
    random.shuffle(a)
    return ''.join(a[:length])


def get_uuid():
    """
    基于时间戳+随机字符串获取到的 UUID
    :return: uuid string
    """
    timestamp = time.time()
    random_str = generate_random_str()
    hash_string = hashlib.md5(str(timestamp) + random_str).hexdigest().upper()
    uuid_string = str(uuid.uuid3(uuid.NAMESPACE_DNS, hash_string))
    return uuid_string.replace('-', '')


if __name__ == '__main__':
    print get_uuid()
