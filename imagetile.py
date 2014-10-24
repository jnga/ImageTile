#!/usr/bin/env python

'''Create a large image by tiling a source image:

    imagetile.py source_file.jpg 3

    outputs: source_file_x3.jpg (3 x 3 grid of the source image, copied)
'''

import os
import sys

from PIL import Image


def main():
    if len(sys.argv) < 2:
        print('Usage: imagetile.py source_image_path multiplier')
        exit(0)
    else:
        source_image_path = sys.argv[1]
        multiplier = int(sys.argv[2])
        path, ext = os.path.splitext(source_image_path)
        output_image_path = path + '_x' + str(multiplier) + ext

        source_image = Image.open(source_image_path)
        (width, height) = source_image.size

        # Create a new image with the requested multiplied size.
        output_image = Image.new('RGBA',
            (width * multiplier, height * multiplier))

        # Paste the source image multiple times into the new output image.
        for row in range(0, multiplier):
            for col in range(0, multiplier):
                box = (col * width, row * height)
                output_image.paste(source_image, box)

        output_image.save(output_image_path)

        print('Done: saved {0}'.format(output_image_path))


if __name__ == '__main__':
    main()
