# Hello,Map!
Hello,Map! is a generator for the most basic framework of a web-based map, including a custom tiled basemap image, icons, and a toggleable legend.

## Requirements
  - Python 3
  - [Pillow Python Imaging Library](https://pypi.python.org/pypi/Pillow/3.0.0)
  - simple local web server for testing (e.g., [http-server](https://www.npmjs.com/package/http-server))

## Usage

### Config
Configuration parameters are defined in `hello-map-config.yml` for many app features.

### Generating tiles
To generate tiles, simply run:
```shell
  python lib/tile_image.py
```
This will create a standard tiled image directory tree at `./app/tiles` using the standard `/{z}/{x}/{y}.png` path structure (`./app/tiles/2/1/0.png`)

Tiling is configured to begin at zoom level 1, breaking the image up into a 2x2 grid of 256px x 256px tiles, and continuing on to the zoom level that allows the image to be rendered at its original resolution in 256px x 256px tiles. For example, an image that is 3300px x 2000px would need 13 x 8 256px x 256px tiles.  This would be supported at zoom level 4 which covers 16 x 16 tiles.

Caution!!! This app can create a very large number of files and data depending on the size of the image (https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames)

### Generating template webmap
To generate the template webmap, simply run:
```shell
  python lib/build_webmap.py
```
This will create a new landing page at `app/index.html`.

### Running app
Point your http server folder to the `app/` folder and open in browser. If using *http_server*, this is just `http-server ./app/`.

### Attributions
The example image `examples/oblique_aerial_image.tif` is included by permission of its owner, me, [Jonathan Dandois](https://github.com/jondandois).
