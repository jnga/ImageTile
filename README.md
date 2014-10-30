# ImageTile

ImageTile is a routine that tiles an image in order to make a larger
one.

It was written to help test web applications that allow uploading
images. The goal was to make image files similar in size to ones from
higher megapixel digital cameras.

It runs on Python, either as a script or from a program. It has been
tested on Python versions 3.4 and 2.7. It relies on the Python Imaging
Library (PIL) fork Pillow.

This project is licensed under the terms of the MIT License.


## Setup on Python 3.4 and higher

1. Change to the directory containing imagetile.py.

2. Create a virtual environment: `pyvenv-3.4 env`

3. Activate the environment: `source env/bin/activate`

4. Install the required packages: `pip install -r requirements.txt`


## Setup on Python 2.7 through 3.3

1. Ensure you have virtualenv installed: `virtualenv`

2. Change to the directory containing imagetile.py.

3. Create a virtual environment: `virtualenv env2`

4. Activate the environment: `source env2/bin/activate`

5. Install the required packages: `pip install -r requirements.txt`


## Running as a script

Enter: `python imagetile.py {source/path/file} {multiplier}`

Example: `python imagetile.py my_dir/mytestfile.jpg 3`

The tiled image is saved to the same directory, with a filename based on
the original appended with _x{multiplier}.

Example output: `Done: saved mytestfile_x3.jpg`


## Using from a program

Example:

	from imagetile import tile_image

	# ...
	
	output_image = tile_image(source_image_path, 3)
	output_image.save(output_image_path)
	

## Running the tests

All tests: `python test_imagetile.py`

A single test: 
`python test_imagetile.py TestImageTile.{test_function_name}`