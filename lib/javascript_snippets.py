import utils as utils

# return the default Leaflet cdns
def leaflet_cdns():
  return """
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css" integrity="sha512-Rksm5RenBEKSKFjgI3a41vrjkw4EVPlJ3+OiI65vTjIdo9brlAacEuKOiQ5OFh7cOI1bkDwLqdLw3Zg0cRJAAQ==" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js" integrity="sha512-/Nsx9X4HebavoBvEBuyp3I7od5tA0UzAxs+j83KgC8PU0kgB4XiK4Lfe4y4cgBtaRJQEIFCW+oC506aPT2L1zw==" crossorigin=""></script>
  """

def leaflet_init(map_config):
  lat = utils.deep_get(map_config, ['center', 'lat'], 0)
  lng = utils.deep_get(map_config, ['center', 'lng'], 0)
  zoom = utils.deep_get(map_config, ['zoom'], 5)
  nowrap = utils.deep_get(map_config, ['nowrap'], True)
  minzoom = utils.deep_get(map_config, ['minzoom'], 18)
  maxzoom = utils.deep_get(map_config, ['maxzoom'], 18)
  attribution = utils.deep_get(map_config, ['attribution'], '')
  url = utils.deep_get(map_config, ['url'], '')

  return """
    // marker Click callback
    var onMarkerClick = function (ev) {
      var marker = ev.target;
      console.log('Clicked: ', marker.options.marker_type);
    };

    // build the map
    let map = L.map('map', {
      center: [%f, %f],
      zoom: %u
    });
    // add a base map
    let OpenStreetMap_BlackAndWhite = L.tileLayer('%s', {
      noWrap: %u,
      minZoom: %u,
      maxZoom: %u,
      attribution: '%s'
    }).addTo(map);
  """%(lat, lng, zoom, url, nowrap, minzoom, maxzoom, attribution)


def leaflet_marker(marker_options):
  marker_type = marker_options['type']
  icon = marker_options['icon']
  lat = marker_options['lat']
  lng = marker_options['lng']
  popup_text = marker_options['popup_text'] or ''
  marker_svg = './assets/%s'%icon
  return """
    // define a new marker
    icon = L.icon({
      iconUrl: '%s',
      iconSize: [30, 30],
      iconAnchor: [15, 30],
      popupAnchor: [0, -30],
    });

    // add a marker
    L.marker([%f, %f],{icon: icon, marker_type: '%s'})
      .bindPopup(%s)
      .on('click', onMarkerClick)
      .addTo(map);
  """%(marker_svg, lat, lng, marker_type, popup_text)


def leaflet_init_legend(legend_items):
  n_items = len(legend_items)
  legend = ""
  if (n_items > 0):
    legend = """
    var legend = L.control({position: 'bottomright'});
    legend.onAdd = function (map) {
      var div = L.DomUtil.create('div', 'info legend');
      var legend_html = '';

      legend_html += '<section>';
      legend_html += '<div><h3 class="legend-title">Legend</h3></div>';
    """

    item_array = (', ').join(["'%s'"%item for item in legend_items])
    item_array = '[%s]'%item_array
    legend +=  """
      %s.map( (item) => {
        legend_html += `<div class="legend-item"><input value="${item}" type="checkbox" checked>`;
        legend_html += `<span class="icon-${item}"></span>&nbsp<span class="label">${item}</span></div>`;
      });
    """%(item_array)

    legend += """
      legend_html += '</section>';

      div.innerHTML = legend_html;
      return div;
    }
    legend.addTo(map);
    """
  return legend
