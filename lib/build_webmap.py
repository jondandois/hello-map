import os
from shutil import copyfile
import config
import javascript_snippets as js_snippets
import utils as utils
config = config.config

# configure the workspace env
ws_dirs = ['./app', './app/css/', './app/tiles/']
[utils.make_dirs_if_not(ws_dir) for ws_dir in ws_dirs]
image = utils.open_image(utils.deep_get(config, ['tile_image', 'image_path'], None))

# read in the index.html.template
with open(os.path.join(os.getcwd(), 'templates', 'index.html.template'), 'r') as f:
  index_html = f.read()
f.closed

# copy over css
example_css = os.path.join(os.getcwd(), 'examples', 'css', 'main.css')
main_css = os.path.join(os.getcwd(), 'app', 'css', 'main.css')
copyfile(example_css, main_css)

# copy over assets
example_assets = os.path.join(os.getcwd(), 'examples', 'assets')
main_assets = os.path.join(os.getcwd(), 'app', 'assets')
utils.copy_dir(example_assets, main_assets)

# add any cdns
cdns = ''
cdns += js_snippets.leaflet_cdns()
index_html = index_html.replace('$cdns', cdns)

# add scripts
scripts = ''

# initialize leaflet
scripts += js_snippets.leaflet_init(config['map_init'])

# draw in markers
markers = config['markers']
width, height = image.size
if markers:
  for marker in markers:
    marker_lng = utils.marker_x_to_lng(marker['x'], width)
    marker_lat = utils.marker_y_to_lat(marker['y'], width)
    scripts += js_snippets.leaflet_marker({
      'type': marker['type'],
      'icon': config['legend'][marker['type']]['icon'],
      'lat': marker_lat,
      'lng': marker_lng,

      'popup_text': "'%s:</br>x: %u, y:%u</br>'"%(marker['type'], marker['x'], marker['y'])
      })

# add the legend
scripts += js_snippets.leaflet_init_legend(config['legend'])

index_html = index_html.replace('$scripts', scripts)

# write to app folder
index_html_out = os.path.join(os.getcwd(), 'app', 'index.html')
output = open(index_html_out, 'w')
output.write(index_html)
output.close

print('new index.html file created in ./app')
print('to view in browser:')
print('open app/index.html')
