import os
import math
from shutil import copyfile
import numpy as np
import utils as utils
import config

###########################################
# determine if image is width major, height major, or square
# and return the resize to tuple
def resize_dims(width, height, dim):
  if width < height: # image taller than wider
    return (int(dim*(width/height)), dim)
  elif width > height: # image wider than tall
    return (dim, int(dim*(height/width)))
  else: # image is square
    return (dim, dim)

###########################################

# get config
config = config.config

image = utils.open_image(utils.deep_get(config, ['tile_image', 'image_path'], None))

#
tile_size = utils.deep_get(config, ['tile_image', 'tile_size'], 256)
width, height = image.size
print((width, height), width/height)
tiles_width = width/tile_size
tiles_height = height/tile_size
max_tile_width = math.ceil(tiles_width)
max_tile_height = math.ceil(tiles_height)

print('columns: %u'%max_tile_width, 'rows: %u'%max_tile_height, ' - max size of %u tile grid'%(tile_size))

# find the highest zoom level that would capture the max number of tiles
max_zoom = 0
for i in range(1,21):
  if max([max_tile_width, max_tile_height]) <= 2**i:
    max_zoom = i
    break

print('max_zoom_needed: %u\n'%max_zoom)

print('making tiles!!!!')
example_tile = os.path.join(os.getcwd(), 'examples', 'earthrender_square.png')

# {z}/{x}/{y}.png
# start at zoom level 1, because 2 x 2
tile_root = os.path.join(os.getcwd(),'app', 'tiles')
utils.make_dirs_if_not(tile_root)

for j in range(1, max_zoom + 1):
  tile_n = 2**j
  max_dim = tile_n * tile_size
  new_size = resize_dims(width, height, max_dim)
  image_resize = image.resize(new_size)

  folder_z = os.path.join(tile_root, '%u'%j)
  utils.make_dirs_if_not(folder_z)

  for x in range(tile_n):
    folder_x = os.path.join(folder_z, '%u'%x)
    utils.make_dirs_if_not(folder_x)

    for y in range(tile_n):
      y_file = os.path.join(folder_x, '%u.png'%y)
      print('zoom: %u'%j, x, y)
      bbox = (x * tile_size, y * tile_size, (x+1)*tile_size, (y+1)*tile_size)
      try:
        tile = image_resize.crop(bbox)
        tile.save(y_file)
      except:
        print('Error making tile, might be out of bounds')
