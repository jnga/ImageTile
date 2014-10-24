#!/usr/bin/env python

"""imagetile.py: tile an image to make a larger image.

    Run as a script at the command line:

    python imagetile.py my_dir/source_file.jpg 3

    output: source_file_x3.jpg (3 x 3 grid of the source image, copied)

    Or use the included tile_image function in a program:

        from imagetile import tile_image

        # ...
        
        output_image = tile_image(source_image_path, 3)
        output_image.save(output_image_path)
"""

import os
import sys

from PIL import Image


def tile_image(source_image_path, multiplier):
    """Tile a source image multiple times, returning a larger image."""
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

    return output_image


def main():
    if len(sys.argv) < 2:
        print('Usage: python imagetile.py source_image_path multiplier')
        exit(0)
    else:
        source_image_path = sys.argv[1]
        multiplier = int(sys.argv[2])
        path, ext = os.path.splitext(source_image_path)
        output_image_path = path + '_x' + str(multiplier) + ext
        output_image = tile_image(source_image_path, multiplier)
        output_image.save(output_image_path)
        print('Done: saved {0}'.format(output_image_path))


if __name__ == '__main__':
    main()
