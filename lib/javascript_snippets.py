import utils as utils

# return the default Leaflet cdns
def leaflet_cdns():
  return """
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.1.0/dist/leaflet.css" integrity="sha512-wcw6ts8Anuw10Mzh9Ytw4pylW8+NAD4ch3lqm9lzAsTxg0GFeJgoAtxuCLREZSC5lUXdVyo/7yfsqFjQ4S+aKw==" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.1.0/dist/leaflet.js" integrity="sha512-mNqn2Wg7tSToJhvHcqfzLMU6J4mkOImSPTxVZAdo+lcPlk+GhZmYgACEe0x35K7YzW1zJ7XyJV/TT1MrdXvMcA==" crossorigin=""></script>
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
