# Tileserver Mapping

This is a django application whose role it is to keep track of available 
[Tileservers](https://github.com/Map-Data/regiontileserver), the region which each one provides data for and 
route incoming traffic to the correct one.

## Map-Data Component Description
Map-Data consists of multiple source repositories which perform different functions.
This section describes how they play together and why they are needed.

The components are:
- [tileserver-mapping](https://github.com/Map-Data/tileserver-mapping) - This application, management and routing
- [osm-tile-data-extract](https://github.com/Map-Data/osm-tile-data-extract) - 
    Scripts to process upstream osm data into usable formats
- [regiontileserver](https://github.com/Map-Data/regiontileserver) - Host a small region as vector tile server
- [map-data.de](https://github.com/Map-Data/map-data.de) - [Website](https://map-data.de/)

**tileserver-mapping** started out as basically only a router which took incoming requests and internally redirected
nginx to the correct *regiontileserver* which is still its main purpose. It now serves the additional role
of managing the data update process and serving sql dumps for *regiontileserver* to use (WIP).

**osm-tile-data-extract** downloads the [Planet Dump](https://wiki.openstreetmap.org/wiki/Planet.osm) from upstream 
OpenStreetMap servers and splits them into smaller parts so that these smaller parts can be processed easier and in a
distributed way. These smaller planet dumps are also uploaded to the *tileserver-mapping* (WIP).
After the upload, one such small dump can be taken and converted to a PostgreSQL Dump which a *regiontileserver* can
later use (WIP). These SQL dumps are then also uploaded to the *tileserver-mapping* (WIP).

**regiontileserver**  is the server which actually provides vector tiles. It does so only for a small region which
can be configured. On startup it downloads an PostgreSQL Dump from *tileserver-mapping* and uses that as its data 
source.

## Configuration
Since this is a Django application, the configuration is all done via a `tileservermapping/settings.py` file.
An example file exists at `tileservermapping/settings.py.example` which is also the one used in our docker image.

That one is set up so that the application can be configured by environment variables:

Environment Variable | Default Value | Description
---------------------|---------------|------------
TM\_DEBUG | *empty* | Enables django debug mode when not empty
TM\_SECRET\_KEY | v€ry $ecret key | [**Change this in production**](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-SECRET_KEY)
TM\_HOSTS | localhost | Comma sperated list of hostnames which this server responds to
TM\_DB\_HOST | localhost | Hostname of the postgresql database server
TM\_DB\_PORT | 5432 | Database port
TM\_DB\_NAME | osm_tileservermapping | Which database to use on that postgresql server
TM\_DB\_USER | osm_tileservermapping | User used to authenticate at the database
TM\_DB\_PASSWORD | osm_tileservermapping | Password of the database user
