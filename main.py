import os

from tqdm import tqdm
from PIL import Image, ExifTags, ImageDraw, ImageFont
from PIL.ExifTags import TAGS

ENCODING = 'utf-8'

def get_file_list(path):
    """
    获取 jpg 文件列表
    :param path: 路径
    :return: 文件名
    """

    # 指定文件后缀名
    extensions = ('.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG')

    imgs = []
    for file_name in os.listdir(dir_path):
        if file_name.endswith(extensions):
            imgs.append(file_name)

    return imgs

def get_exif(img):
    """
    获取exif的光圈 快门 iso
    :param img: 照片
    :return: exif信息
    """
    ret = {}
    if hasattr(img, '_getexif'):
        exifinfo = img._getexif()
        for tag, value in exifinfo.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        
        # 检查三要素
        iso = ret.get('ISOSpeedRatings')
        f = ret.get('FNumber')
        t = ret.get('ExposureTime')
    
        if iso and f and t:
            return [str(iso), str(f), float(t)]
        else:
            return None
    else:
        return None

def add_shutter(t, watermark):
    draw = ImageDraw.Draw(watermark)
    
    if t < 1.0:
        text = "1/" + str(int(1 / t))
    else:
        text = str(t) + '\'\''

    font = ImageFont.truetype('arial.ttf', 150)  # 字体
    left, top, right, bottom = draw.textbbox((0, 0), text, font)  # 计算文本的宽度和高度
    text_width, text_height = right - left, bottom - top

    pos_x = 0  # x轴位置（左对齐）
    pos_x += (watermark.width - pos_x - text_width) // 2 - 1500 # 计算水平中心对齐的偏移量
    pos_y = watermark.height - text_height - 355  # y轴位置（底部对齐）

    color = (255, 255, 255) 
    draw.text((pos_x, pos_y), text, color, font=font)

def add_iso(iso, watermark):
    draw = ImageDraw.Draw(watermark)
    color = (255, 255, 255) 

    text = "ISO"
    font = ImageFont.truetype('arial.ttf', 100)  # 字体
    draw.text((5520, 6000), text, color, font=font)


    text = iso
    font = ImageFont.truetype('arial.ttf', 150)  # 字体
    left, top, right, bottom = draw.textbbox((0, 0), text, font)  # 计算文本的宽度和高度
    text_width, text_height = right - left, bottom - top
    pos_x = 0  # x轴位置（左对齐）
    pos_x += (watermark.width - pos_x - text_width) // 2 + 1600 # 计算水平中心对齐的偏移量
    pos_y = watermark.height - text_height - 355  # y轴位置（底部对齐）
    draw.text((pos_x, pos_y), text, color, font=font)

def add_fnumber(f, watermark):
    draw = ImageDraw.Draw(watermark)
    color = (255, 255, 255) 
    
    text = "F/"
    font = ImageFont.truetype('arial.ttf', 120)  # 字体
    draw.text((4150, 6050), text, color, font=font)

    text = f
    font = ImageFont.truetype('arial.ttf', 150)  # 字体
    left, top, right, bottom = draw.textbbox((0, 0), text, font)  # 计算文本的宽度和高度
    text_width, text_height = right - left, bottom - top
    pos_x = 0  # x轴位置（左对齐）
    pos_x += (watermark.width - pos_x - text_width) // 2 + 100 # 计算水平中心对齐的偏移量
    pos_y = watermark.height - text_height - 350  # y轴位置（底部对齐）
    draw.text((pos_x, pos_y), text, color, font=font)



def merge_imgs(img, watermark, img_filename):
    img = img.convert("RGBA")

    if img.size != watermark.size:
        watermark = watermark.resize(img.size)

    blended_img = Image.alpha_composite(img, watermark)
    blended_img = blended_img.convert("RGB")

    filename = "./outputs/" + img_filename
    blended_img.save(filename)





if __name__ == "__main__":
    # 指定目录路径
    dir_path = './inputs'

    imgs = get_file_list(dir_path)

    failed_imgs = []

    for img_filename in tqdm(imgs):
        img = Image.open(dir_path + '/' + img_filename)

        img_w, img_h = img.size
        if img_w >= img_h:
            exif = get_exif(img)
            watermark = Image.open('watermark1.png')
            
            # 检查是否包含exif信息
            if exif is not None:
                iso, f, t = exif[0], exif[1], exif[2]

                add_iso(iso, watermark)
                add_fnumber(f, watermark)
                add_shutter(t, watermark)

                merge_imgs(img, watermark, img_filename)
            else:
                failed_imgs.append(img_path)

        else:
            # TODO
            pass



    print("添加水印失败图像:", failed_imgs)