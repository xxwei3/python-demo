# 通过pillow库实现图像处理操作

from PIL import Image
from PIL import ImageFilter


def operate_image_1(path):
    """打开，复制原图，缩放图片，展示"""
    original_img = Image.open(path)
    print(f'operate_image_1 open source image {path}, format={original_img.format}, size={original_img.size}, mode={original_img.mode}')
    copy_img = original_img.copy()
    copy_img.thumbnail((400, 300))  # 指定缩放的尺寸
    copy_img.show()
    print(f'operate_image_1 open dest image , format={copy_img.format}, size={copy_img.size}, mode={copy_img.mode}')


def operate_image_2(path):
    """打开，复制原图，重置图片，展示"""
    original_img = Image.open(path)
    print(f'operate_image_2 open source image {path}, format={original_img.format}, size={original_img.size}, mode={original_img.mode}')
    copy_img = original_img.copy()
    resize_img = copy_img.resize((400, 300))  # 指定重置的尺寸
    resize_img.filter(ImageFilter.GaussianBlur)  # 加个滤镜
    resize_img.show()
    print(f'operate_image_2 open dest image , format={resize_img.format}, size={resize_img.size}, mode={resize_img.mode}')


def operate_image_3(path):
    """"剪切原图，并黏贴到指定区域"""
    original_img = Image.open(path)
    print(f'operate_image_3 open source image {path}, format={original_img.format}, size={original_img.size}, mode={original_img.mode}')
    copy_img = original_img.copy()
    # 指定区域进行剪切
    crop_img = copy_img.crop((5, 5, 150, 150))
    # 新建一个底图，用于放置剪切图像
    bottom_img = Image.new(mode='RGB', size=(700, 500), color='green')
    bottom_img.paste(crop_img, (100, 100))
    bottom_img.show()
    print(f'operate_image_3 open dest image , format={crop_img.format}, size={crop_img.size}, mode={crop_img.mode}')


if __name__ == '__main__':
    img_path = 'D:\\My Test\\XXX\\test-image\\IMG_20220708_122825.jpg'
    operate_image_1(img_path)
    operate_image_2(img_path)
    operate_image_3(img_path)
