#!/usr/bin/env python
from PIL import Image, ImageFont, ImageDraw
from inky import InkyPHAT

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne

font = ImageFont.truetype(FredokaOne, 22)

message = "I love you Sem"
w, h = font.getsize(message)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), message, inky_display.RED, font)
inky_display.set_image(img)
inky_display.show()


# import sys
# from inky import InkyPHAT
# from PIL import Image, ImageFont, ImageDraw
# from font_fredoka_one import FredokaOne

# inky_display = InkyPHAT("red")
# inky_display.set_border(inky_display.WHITE)
#
# img = Image.open("/home/pi/unconf.png")
#
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(FredokaOne, 22)
#
# message = sys.argv[1] if len(sys.argv) > 1 else "UnConf"
# w, h = font.getsize(message)
# x = ((inky_display.WIDTH - w) / 2)
# y = ((inky_display.HEIGHT - h) / 2)
# draw.text((x, y), message, inky_display.WHITE, font)
#
# inky_display.set_image(img)
# inky_display.show()
