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

  # get marker position relative to web mercator size
  marker_y_pos = marker_y / image_height
  mercator_y_top = 20037508.34
  mercator_y_range = mercator_y_top * 2
  marker_y_mercator = ((marker_y_pos * mercator_y_range) - mercator_y_top) * -1

  # convert this to latitude via ellipitcal projection
  marker_lat = merc_2_lat(marker_y_mercator)
  return marker_lat


# adapted from https://wiki.openstreetmap.org/wiki/Mercator#JavaScript_.28or_ActionScript.29_implementation
def merc_2_lat(merc_y):
  import math
  r_major = 6378137.0 # Equatorial Radius, WGS84
  r_minor = 6356752.314245179 # defined as constant
  temp_r = r_minor / r_major
  e = math.sqrt(1.0 - temp_r**2) # eccentricity of earth ellipse

  lat = math.degrees(pj_phi2( math.exp( 0-(merc_y/r_major)), e))
  return lat

# adapted from https://wiki.openstreetmap.org/wiki/Mercator#JavaScript_.28or_ActionScript.29_implementation
def pj_phi2(ts, e):
  import math
  n_iter = 15
  half_pi= math.pi/2

  tol = 0.0000000001
  eccnth = 0.5 * e
  phi = half_pi - 2.0 * math.atan(ts)
  dphi = 1
  i = 1
  while abs(dphi) > tol and i < n_iter:
    con = e * math.sin(phi)
    dphi = half_pi - 2.0 * math.atan(ts * math.pow((1. - con) / (1. + con), eccnth)) - phi
    phi += dphi
    i += 1
  return phi;


'''
  copy a directories and contents
'''
def copy_dir(src, dest):
  import errno
  import shutil
  try:
    shutil.copytree(src, dest)
  except OSError as e:
    # If the error was caused because the source wasn't a directory
    if e.errno == errno.ENOTDIR:
      shutil.copy(src, dest)
    else:
      print('Directory not copied. Error: %s' % e)
