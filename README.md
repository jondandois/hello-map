# Hello,Map!
Hello,Map! is a generator for the most basic framework of a web-based map, including a custom tiled basemap image, icons, and a toggleable legend.

## Requirements
  - Python 3
  - simple local web server for testing (e.g., [http-server](https://www.npmjs.com/package/http-server))

## Usage

### Config
Configuration parameters are defined in `hello-map-config.yml` for many app features.

### Generating tiles

### Generating template webmap
To generate the template webmap, simply run:
```shell
  python lib/build_webmap.py
```
This will create a new landing page at `app/index.html`. Simply open this file in a browser or point your http server folder to the `app/` folder.

### Attributions
The example image `examples/oblique_aerial_image.tif` is included by permission of its owner, me, [Jonathan Dandois](https://github.com/jondandois).

### License
Hello,Map! is licensed under GNU GPL3.0. A copy of that license is distributed with this software.

This software makes use of [Leaflet APIs](https://github.com/Leaflet/Leaflet) and may also be subject to its TOC.
