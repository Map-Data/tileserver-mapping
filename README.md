# Tileserver Mapping

This is a django application whose role it is to keep track of available 
[Tileservers](https://github.com/Map-Data/regiontileserver), the region which each one provides data for and 
route incoming traffic to the correct one.

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
TM\_MEDIA\_ROOT | /app/media | Where uploaded files are stored
TM\_DB\_PORT | 5432 | Database port
TM\_DB\_NAME | osm_tileservermapping | Which database to use on that postgresql server
TM\_DB\_USER | osm_tileservermapping | User used to authenticate at the database
TM\_DB\_PASSWORD | osm_tileservermapping | Password of the database user

