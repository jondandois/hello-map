import os
import yaml
# read in the basemap config
config = {}
with open(os.path.join(os.getcwd(), 'hello-map-config.yml'), 'r') as f:
  config = yaml.load(f.read())
