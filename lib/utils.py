'''
  safe traverse a dict
  nested = {'a': {'b': {'c': 42}}}

  print deep_get(nested, ['a', 'b'])
  print deep_get(nested, ['a', 'b', 'z', 'z'], default='missing')
'''
def deep_get(_dict, keys, default=None):
  for key in keys:
      if isinstance(_dict, dict):
          _dict = _dict.get(key, default)
      else:
          return default
  return _dict

'''
  Make a directory if it does not already exist
'''
def make_dirs_if_not(in_dir):
  import os
  if not os.path.exists(in_dir):
    os.makedirs(in_dir)

'''
  try to open an image from a path and return it if successful
  if fail, process exit since there is no point in continuing
'''
def open_image(image_path):
  import os
  from PIL import Image

  try:
    image_full_path = os.path.join(os.getcwd(), image_path)
    image = Image.open(image_full_path)
    print('Sucessfully read in image\n')
    return image
  except:
    print('Image could not be found or read, exiting')
    exit(1)

'''
  Compute the longitude from a marker image coordinate
'''
def marker_x_to_lng(marker_x, image_width):
  marker_x_pos = marker_x/image_width
  if marker_x_pos == 0.5:
    marker_lng = 0
  elif marker_x_pos < 0.5:
    marker_lng = (180 * marker_x_pos) - 180
  else:
    marker_lng = 180 * marker_x_pos
  return marker_lng

'''
  Compute the latitude from a marker image coordinate
'''
def marker_y_to_lat(marker_y, image_height):
  import math
  marker_y_pos = marker_y/image_height
  y_max = math.degrees(math.atan(math.sinh(math.pi)))
  if marker_y_pos == 0.5:
    marker_lat = 0
  elif marker_y_pos < 0.5:
    marker_lat = (y_max * marker_y_pos) - y_max
  else:
    marker_lat = -(y_max * marker_y_pos)
  return marker_lat

