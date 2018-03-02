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
  marker_x_pos = marker_x / image_width
  marker_lng = (marker_x_pos * 360) - 180
  return marker_lng

'''
  Compute the latitude from a marker image coordinate
'''
def marker_y_to_lat(marker_y, image_height):
  import math
  y_max = math.degrees(math.atan(math.sinh(math.pi)))
  y_range = y_max * 2

  print(y_max, y_range)
  marker_y_pos = marker_y / image_height
  print (marker_y, marker_y_pos)
  marker_lat = ((marker_y_pos * y_range) - y_max) * -1
  return marker_lat
