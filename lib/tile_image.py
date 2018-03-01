import os
import numpy as np
from PIL import Image
import utils as utils
import config

# get config
config = config.config

# TODO: break up this try catch do make it easier to debug
try:
  image_path = os.path.join(os.getcwd(), utils.deep_get(config, ['tile_image', 'image_path'], None))
  image = Image.open(image_path)
  print(image)
  tile_size = utils.deep_get(config, ['tile_image', 'tile_size'], 256)
  width, height = image.size
  tiles_width = width/tile_size
  tiles_height = height/tile_size
  print(tiles_width, tiles_height)
except:
  print('Image could not be found, exiting')
  exit(1)
