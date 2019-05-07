from PIL import ImageFont

def bold(size=12):
    return ImageFont.truetype("./fonts/bold.ttf", size) 
def regular(size=12):
    return ImageFont.truetype("./fonts/regular.ttf", size)