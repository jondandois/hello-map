import os
import config
import javascript_snippets as js_snippets
import utils as utils
config = config.config

# configure the workspace env
ws_dirs = ['./app']
[utils.make_dirs_if_not(ws_dir) for ws_dir in ws_dirs]
image = utils.open_image(utils.deep_get(config, ['tile_image', 'image_path'], None))

# read in the index.html.template
with open(os.path.join(os.getcwd(), 'templates', 'index.html.template'), 'r') as f:
  index_html = f.read()
f.closed

# add any cdns
cdns = ''
cdns += js_snippets.leaflet_cdns()
index_html = index_html.replace('$cdns', cdns)

# add scripts
scripts = ''
scripts += js_snippets.leaflet_init(config['map_init'])
index_html = index_html.replace('$scripts', scripts)

markers = config['markers']
width, height = image.size
for marker in markers:
  marker_lng = utils.marker_x_to_lng(marker['x'], width)
  print(marker['x'], marker_lng)
  marker_lat = utils.marker_y_to_lat(marker['y'], height)
  print(marker['y'], marker_lat)


# write to app folder
index_html_out = os.path.join(os.getcwd(), 'app', 'index.html')
output = open(index_html_out, 'w')
output.write(index_html)
output.close

print('new index.html file created in ./app')
print('to view in browser:')
print('open app/index.html')
