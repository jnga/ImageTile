# ImageTile

ImageTile is a Python script that takes an image file and tiles it in order
to create a larger file.

It was written to help test web applications that allow uploading images.
The goal was to approximate images taken with digital cameras of varying
megapixel specifications.

The script originally ran on Python 2.7 and is now also known to work with
Python 3.4.

## Setup on Python 3.4 and higher

1. Change to the script directory.

2. Create a virtual environment: `pyvenv-3.4 env`

3. Activate the environment: `source env/bin/activate`

4. Install the required libraries: `pip install -r requirements.txt`

5. Run the script: `python imagetile.py {source\path\file} {multiplier}`

Example: `python imagetile.py mytestfile.png 3`
