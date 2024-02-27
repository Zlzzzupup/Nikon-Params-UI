from PIL import Image, ExifTags, ImageDraw, ImageFont
from PIL.ExifTags import TAGS

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

def add_shutter1(t, watermark):
    draw = ImageDraw.Draw(watermark)
    color = (255, 255, 255) 

    if t < 1.0:
        text = "1/" + str(int(1 / t))
    else:
        text = str(t) + '\'\''

    font = ImageFont.truetype('arial.ttf', 150)  # 字体
    left, top, right, bottom = draw.textbbox((0, 0), text, font)  # 计算文本的宽度和高度
    text_width, text_height = right - left, bottom - top
    pos_x = 0  # x轴位置（左对齐）
    pos_x += (watermark.width - pos_x - text_width) // 2 - 2755 # 计算水平中心对齐的偏移量
    pos_y = watermark.height - text_height - 300  # y轴位置（底部对齐）
    draw.text((pos_x, pos_y), text, color, font=font)


def add_fnumber1(f, watermark):
    draw = ImageDraw.Draw(watermark)
    color = (255, 255, 255) 

    text = f
    font = ImageFont.truetype('arial.ttf', 150)  # 字体
    left, top, right, bottom = draw.textbbox((0, 0), text, font)  # 计算文本的宽度和高度
    text_width, text_height = right - left, bottom - top
    pos_x = 0  # x轴位置（左对齐）
    pos_x += (watermark.width - pos_x - text_width) // 2 - 2150 # 计算水平中心对齐的偏移量
    pos_y = watermark.height - text_height - 270  # y轴位置（底部对齐）
    draw.text((pos_x, pos_y), text, color, font=font)

def add_iso1(iso, watermark):
    draw = ImageDraw.Draw(watermark)
    color = (255, 255, 255) 

    text = "ISO"
    font = ImageFont.truetype('arial.ttf', 100)  # 字体
    draw.text((5540, 8230), text, color, font=font)

    text = iso
    font = ImageFont.truetype('arial.ttf', 130)  # 字体
    left, top, right, bottom = draw.textbbox((0, 0), text, font)  # 计算文本的宽度和高度
    text_width, text_height = right - left, bottom - top
    pos_x = 0  # x轴位置（左对齐）
    pos_x += (watermark.width - pos_x - text_width) // 2 + 2650 # 计算水平中心对齐的偏移量
    pos_y = watermark.height - text_height - 315  # y轴位置（底部对齐）
    draw.text((pos_x, pos_y), text, color, font=font)

def add_watermark(exif, watermark):
    iso, f, t = exif[0], exif[1], exif[2]
    add_fnumber(f, watermark)
    add_iso(iso, watermark)
    add_shutter(t, watermark)

    return watermark

def add_watermark1(exif, watermark):
    iso, f, t = exif[0], exif[1], exif[2]
    add_fnumber1(f, watermark)
    add_iso1(iso, watermark)
    add_shutter1(t, watermark)

    return watermark
