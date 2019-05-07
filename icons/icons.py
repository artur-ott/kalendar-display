from PIL import Image, ImageOps
from util.colors import _color

icon_01 = Image.open('./icons/icons_01.bmp')
icon_02 = Image.open('./icons/icons_02.bmp')
icon_03 = Image.open('./icons/icons_03.bmp')
icon_04 = Image.open('./icons/icons_04.bmp')

if (_color == 0):
    icon_01 = ImageOps.invert(icon_01)
    icon_02 = ImageOps.invert(icon_02)
    icon_03 = ImageOps.invert(icon_03)
    icon_04 = ImageOps.invert(icon_04)#


icon_01 = icon_01.convert('1')
icon_02 = icon_02.convert('1')
icon_03 = icon_03.convert('1')
icon_04 = icon_04.convert('1')
    
icon_array = [
    Image.new('1', (0, 0)),
    icon_01,
    icon_02,
    icon_03,
    icon_04
]
