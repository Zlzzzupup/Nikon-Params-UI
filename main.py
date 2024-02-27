import os

from tqdm import tqdm
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS

from utils import add_watermark, add_watermark1

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
        exif = get_exif(img)

        # 检查是否包含exif信息
        if exif is None:
            failed_imgs.append(img_path)
            continue

        if img_w >= img_h:
            watermark = Image.open('watermark1.png')
            add_watermark(exif, watermark)
        else:
            watermark = Image.open('watermark2.png')
            add_watermark1(exif, watermark)

        merge_imgs(img, watermark, img_filename)

    print("添加水印失败图像:", failed_imgs)