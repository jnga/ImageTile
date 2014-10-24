# ImageTile

ImageTile is a Python script that takes an image file and tiles it in order
to create a larger file.

It was written to help test web applications that allow uploading images.
The goal was to approximate files of sizes from digital cameras of varying
megapixel specifications.

The script runs on Python 3 and Python 2, having been tested on versions
3.4 and 2.7. It relies on the Python Imaging Library (PIL) supplied by the
PIL fork Pillow.


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


## Running the script

Enter: `python imagetile.py {source/path/file} {multiplier}`

Example: `python imagetile.py mytestfile.jpg 3`

The tiled image is saved to the same directory, with a filename based on
the original appended with _x{multiplier}.

Example output: `Done: saved mytestfile_x3.jpg`