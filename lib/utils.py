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
