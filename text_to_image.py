from math import ceil
import sys, random, argparse
import numpy as np
import math
from PIL import (
    Image,
    ImageFont,
    ImageDraw,
)
import cv2 as cv

















def textfile_to_image(textfile_path):
    """Convert text file to a grayscale image.

    arguments:
    textfile_path - the content of this file will be converted to an image
    font_path - path to a font file (for example impact.ttf)
    """
    # parse the file into lines stripped of whitespace on the right side
    with open(textfile_path) as f:
        lines = tuple(line.rstrip() for line in f.readlines())

    # choose a font (you can see more detail in the linked library on github)
    font = None
    large_font = 20  # get better resolution with larger size
    for font_filename in COMMON_MONO_FONT_FILENAMES:
        try:
            font = ImageFont.truetype(font_filename, size=large_font)
            print(f'Using font "{font_filename}".')
            break
        except IOError:
            print(f'Could not load font "{font_filename}".')
    if font is None:
        font = ImageFont.load_default()
        print('Using default font.')

    # make a sufficiently sized background image based on the combination of font and lines
    font_points_to_pixels = lambda pt: round(pt * 96.0 / 72)
    margin_pixels = 20

    # height of the background image
    tallest_line = max(lines, key=lambda line: font.getsize(line)[PIL_HEIGHT_INDEX])
    max_line_height = font_points_to_pixels(font.getsize(tallest_line)[PIL_HEIGHT_INDEX])
    realistic_line_height = max_line_height * 0.8  # apparently it measures a lot of space above visible content
    image_height = int(ceil(realistic_line_height * len(lines) + 2 * margin_pixels))

    # width of the background image
    widest_line = max(lines, key=lambda s: font.getsize(s)[PIL_WIDTH_INDEX])
    max_line_width = font_points_to_pixels(font.getsize(widest_line)[PIL_WIDTH_INDEX])
    #image_width = int(ceil(max_line_width + (2 * margin_pixels)))
    image_width = int(ceil(max_line_width ))
    

    # draw the background
    background_color = 0  # white
    image = Image.new(PIL_GRAYSCALE, (image_width, image_height), color=background_color)
    draw = ImageDraw.Draw(image)

    # draw each line of text
    font_color = 5  # black
    horizontal_position = margin_pixels
    for i, line in enumerate(lines):
        vertical_position = int(round(margin_pixels + (i * realistic_line_height)))
        draw.text((horizontal_position, vertical_position), line, fill=font_color, font=font)
    pil_image = image.convert('Gray') 
    open_cv_image = np.array(pil_image) 
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 


    return open_cv_image


















PIL_GRAYSCALE = 'L'
PIL_WIDTH_INDEX = 0
PIL_HEIGHT_INDEX = 1
COMMON_MONO_FONT_FILENAMES = [
    'DejaVuSansMono.ttf',  # Linux
    'Consolas Mono.ttf',   # MacOS, I think
    'Consola.ttf',         # Windows, I think
]

"""
# create parser
descStr = "This program converts txt to png"
parser = argparse.ArgumentParser(description=descStr)
# add expected arguments
parser.add_argument('--file', dest='txtFile', required=True)
parser.add_argument('--out', dest='outFile', required=False)

# parse args
args = parser.parse_args()

txtFile = args.txtFile

# set output file
outFile = 'out.png'
if args.outFile:
    outFile = args.outFile

image = textfile_to_image(txtFile)
image.save(outFile)
img = Image.open(outFile)
rgba = img.convert("RGBA")
datas = rgba.getdata()

newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
        # storing a transparent value when we find a black colour
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)  # other colours remain unchanged
    
rgba.putdata(newData)
rgba.save(outFile, "PNG")


"""

