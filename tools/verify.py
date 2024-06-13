import os
import re


def verify_mobile(mobile):
    """校验手机号合法性，11位数字"""
    pattern = re.compile(r'^1[345789]\d{9}$')
    return pattern.match(mobile)


def verify_mail(mail):
    """校验电子邮件合法性"""
    pattern = re.compile(r'^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$')
    return pattern.match(mail)


def verify_file_path(path):
    """检查目标文件是否存在，不存在新建"""
    if not os.path.exists(path):
        with open(path, 'x', encoding='utf-8'):
            print(f'file path not exists, create new file ----> {path}')
