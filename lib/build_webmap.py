import os
import yaml
import javascript_snippets as js_snippets

# configure the workspace env
ws_dirs = ['./app']
for ws_dir in ws_dirs:
  if not os.path.exists(ws_dir):
    os.makedirs(ws_dir)

# read in the basemap config
with open(os.path.join(os.getcwd(), 'hello-map-config.yml'), 'r') as f:
  config = yaml.load(f.read())

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
scripts += js_snippets.leaflet_init(config['basemap'])
index_html = index_html.replace('$scripts', scripts)

# write to app folder
index_html_out = os.path.join(os.getcwd(), 'app', 'index.html')
output = open(index_html_out, 'w')
output.write(index_html)
output.close

print('new index.html file created in ./app')
print('to view in browser:')
print('open app/index.html')
