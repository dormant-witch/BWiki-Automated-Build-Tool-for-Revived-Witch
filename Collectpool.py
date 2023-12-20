import os

# import 字体相关三件套
from PIL import ImageFont, Image, ImageDraw
from wand.drawing import Drawing

# 生成font
ttf_path = r'新建文件夹\fzzzhGBKjf.ttf'
text_size = 33 # text_size 是字号
font = ImageFont.truetype(ttf_path, text_size)
print(font.getbbox('2023/04/13 14:00 - 2023/04/17 03:59')[2])
print(font.getbbox('2023/04/23 14:00 - 2023/04/27 03:59'))
print(font.getbbox('2023/04/27 14:00 - 2023/05/04 03:59'))
#


from wand.color import Color
from wand.image import Image
from wand.drawing import Drawing
from wand.compat import nested
from math import cos, pi, sin

with nested(Color('lightblue'),
            Color('transparent'),
            Drawing()) as (bg, fg, draw):
    # draw.stroke_width = 3
    # draw.fill_color = fg
    # for degree in range(0, 360, 15):
    #     draw.push()  # Grow stack
    #     draw.stroke_color = Color('hsl({0}%, 100%, 50%)'.format(degree * 100 / 360))
    #     t = degree / 180.0 * pi
    #     x = 35 * cos(t) + 50
    #     y = 35 * sin(t) + 50
    #     draw.line((50, 50), (x, y))
    #     draw.pop()  # Restore stack

    draw.font = ttf_path
    draw.font_size = 33
    # draw.text_under_color=bg
    draw.fill_color= Color('RGBA(0, 0, 0,0.3)')
    draw.rectangle(left=203-6, top=640, right=203+660+6, bottom=680)
    draw.fill_color= Color('RGBA(255, 255, 255,1)')
    draw.text(203,672, '2023/04/27 14:00 - 2023/05/04 03:59')
    # draw(image)
    with Image(filename='ac2.png') as img:
        draw(img)
        print(img.size)
        img.save(filename='monaZ.png')

indir=r'leiting\整理\小人'
ondir=r'新建文件夹\放大小人'
for i in os.listdir(indir):
    consoleText='magick "{}" -resize 300% -trim "{}"'.format(os.path.join(indir,i),os.path.join(ondir,i))
    print(i)
    os.system(consoleText)
