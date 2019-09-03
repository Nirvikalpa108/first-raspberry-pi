#!/usr/bin/env python

import sys
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.open("/home/pi/unconf.png")

draw = ImageDraw.Draw(img)
font = ImageFont.truetype(FredokaOne, 22)

message = sys.argv[1] if len(sys.argv) > 1 else "UnConf"
w, h = font.getsize(message)
x = ((inky_display.WIDTH - w) / 2)
y = ((inky_display.HEIGHT - h) / 2)
draw.text((x, y), message, inky_display.WHITE, font)

inky_display.set_image(img)
inky_display.show()
