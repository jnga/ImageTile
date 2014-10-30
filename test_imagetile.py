import imagetile
import os
import sys
import unittest

from PIL import Image


class TestImageTile(unittest.TestCase):

    def setUp(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '/test_images/'
        self.jpeg = path + 'spruce.jpg'
        self.png = path + 'spruce.png'
        self.width = 400
        self.height = 300
        self.bytes_per_pixel = 4
        self.formats = ['jpeg', 'png']
        self.output = None
        
    def tearDown(self):
        if self.output is not None:
            self.output.close()
               
    def test_tile_image_handles_jpeg(self):
        with Image.open(self.jpeg) as source:
            self.assertEqual(source.format, 'JPEG')            
        
    def test_tile_image_handles_png(self):
        with Image.open(self.png) as source:
            self.assertEqual(source.format, 'PNG') 

    def test_tile_image_returns_image(self):
        for format in self.formats:
            self.output = imagetile.tile_image(getattr(self, format), 1)
            self.assertTrue(isinstance(self.output, Image.Image))
        
    def test_tile_image_1_returns_same_size(self):
        for format in self.formats:
            self.output = imagetile.tile_image(getattr(self, format), 1)
            self.assertEqual(self.output.size, (self.width, self.height))
        
    def test_tile_image_2_returns_double_size(self):
        for format in self.formats:
            self.output = imagetile.tile_image(getattr(self, format), 2)
            self.assertEqual(self.output.size,
                (self.width * 2, self.height * 2))
        
    def test_tile_image_3_returns_triple_size(self):
        for format in self.formats:
            self.output = imagetile.tile_image(getattr(self, format), 3)
            self.assertEqual(self.output.size,
                (self.width * 3, self.height * 3))

    def test_tile_image_1_returns_identical_image(self):
        for format in self.formats:
            source_path = getattr(self, format)
            with Image.open(source_path).convert('RGBA') as source:
                self.output = imagetile.tile_image(source_path, 1)
                self.assertEqual(source.tobytes(), self.output.tobytes())

    def test_tile_image_2_has_quadruple_the_pixels(self):
        for format in self.formats:
            self.output = imagetile.tile_image(getattr(self, format), 2)
            self.assertEqual(len(self.output.tobytes()),
                self.width * self.height * self.bytes_per_pixel * 4)
            
    def test_tile_image_3_has_nine_times_the_pixels(self):
        for format in self.formats:
            self.output = imagetile.tile_image(getattr(self, format), 3)
            self.assertEqual(len(self.output.tobytes()),
                self.width * self.height * self.bytes_per_pixel * 9)
                
    def test_tile_image_has_identical_pixels(self):
        multiplier = 2
        with Image.open(self.jpeg).convert('RGBA') as source:
            src_pixels = [[None for y in range(self.height)]
                for x in range(self.width)]            
            self.output = imagetile.tile_image(self.jpeg, multiplier)
            for row in range(0, multiplier):
                for col in range(0, multiplier):
                    for x in range(col * self.width,
                            (col * self.width) + self.width):
                        for y in range(row * self.height,
                                (row * self.height) + self.height):
                            out_pixel = self.output.getpixel((x, y))
                            src_x = x - (col * self.width)
                            src_y = y - (row * self.height)
                            if src_pixels[src_x][src_y] is None:
                                src_pixel = source.getpixel((src_x, src_y))
                                src_pixels[src_x][src_y] = src_pixel
                            else:
                                src_pixel = src_pixels[src_x][src_y]
                            self.assertEqual(out_pixel, src_pixel)


if __name__ == '__main__':
    if sys.version_info[0] >= 3:
        # Ignore Python 3 ResourceWarnings from PIL for now.
        # See https://github.com/python-pillow/Pillow/issues/835
        unittest.main(warnings='ignore')
    else:
        unittest.main()