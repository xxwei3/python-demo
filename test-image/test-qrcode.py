# qrcode模块实现二维码生成器
import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask, SquareGradiantColorMask
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer


def generate_qrcode1(path, data):
    """示例1：快速生成二维码，保存并展示"""
    qr = qrcode.make(data)
    qr.save(path)
    qr.show()


def generate_qrcode2(path, data):
    """示例2：自定义生成二维码，保存并展示"""
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="green", back_color="white")
    img.save(path)
    img.show()


def generate_qrcode3(path, data, logo):
    """示例3：自定义生成二维码，在二维码中间加入图片，保存并展示"""
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert("RGBA")
    # 二维码中间logo图标设置
    icon = Image.open(logo)
    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h))  # 重置logo尺寸
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), mask=None)
    img.save(path)
    img.show()


def generate_qrcode4(base_path4, data, logo, sel):
    """示例4：自定义生成二维码的样式"""
    print(f'start generate_qrcode4, ............  sel={sel}')
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    if sel == '1':
        # 修改二维码形状
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    elif sel == '2':
        # 修改二维码颜色
        img = qr.make_image(image_factory=StyledPilImage, color_mask=SquareGradiantColorMask())
    elif sel == '3':
        # 嵌入图像
        img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=logo)
    else:
        # 嵌入图像
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer(),
                            color_mask=RadialGradiantColorMask(), embeded_image_path=logo)
    img.save(base_path4)
    # img.show()
    print(f'end generate_qrcode4, ............  base_path={base_path4}')


if __name__ == '__main__':
    base_path = 'D:\\My Test\\XXX\\test-image\\'
    base_path1 = base_path + 'qr_hello_1.png'
    base_path2 = base_path + 'qr_hello_2.png'
    base_path3 = base_path + 'qr_hello_3.png'
    logo = base_path + 'girl.jpg'
    data = 'hello world!'
    generate_qrcode1(base_path1, data)
    generate_qrcode2(base_path2, data)
    generate_qrcode3(base_path3, data, logo)
    for i in range(0, 4):
        sel = str(i + 1)
        generate_qrcode4(base_path + f'qr_style_{sel}.png', data, logo, sel=sel)
