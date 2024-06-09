# barcode模块实现条形码生成器,svg和图片格式

import os
import random

from barcode import EAN13
from barcode.writer import SVGWriter, ImageWriter


def check_path(file_path):
    """检查目标文件是否存在，不存在新建"""
    if not os.path.exists(file_path):
        with open(file_path, 'x', encoding='utf-8'):
            print(f'file path not exists, create new file ----> {file_path}')


def generate_svg_barcode(base_path, message):
    full_path = base_path + message + ".svg"
    check_path(full_path)
    # 注意：必须要wb模式写入，EAN13标准对message字符串的位数至少是8位
    with open(full_path, 'wb') as f:
        EAN13(message, writer=SVGWriter()).write(f)


def generate_image_barcode(base_path, message):
    # 图片格式随机选择
    format_list = ['jpg', 'jpeg', 'JPG', 'JPEG', 'png', 'PNG']
    full_path = base_path + message + "." + format_list[random.randint(0, len(format_list) - 1)]
    check_path(full_path)
    # 注意：必须要wb模式写入，EAN13标准对message字符串的位数至少是8位
    with open(full_path, 'wb') as f:
        EAN13(message, writer=ImageWriter()).write(f)


if __name__ == '__main__':
    base_path = 'D:\\My Test\\XXX\\test-image\\'
    message = '10001' + str(random.randint(10000001, 99999999))
    generate_svg_barcode(base_path, message)
    generate_image_barcode(base_path, message)
