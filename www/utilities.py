from urllib.request import urlopen
from json import loads as json_loads
from data.models import Location, Record

def grab_location_data(place_id):
    location_url = "https://nominatim.openstreetmap.org/details.php?place_id=%d&format=json&limit=1&polygon_geojson=1" % place_id
    
    data = None
    with urlopen(location_url) as url:
        data = json_loads(url.read().decode())
    
    return data

def record_update_with_location(record_id, place_id):
    try:
        location = Location.objects.get(place_id=place_id)
    except Location.DoesNotExist:
        details = grab_location_data(place_id)
        location = Location(
            place_id=int(details["place_id"]),
            display_name=details['localname'],
            lat=details["centroid"]["coordinates"][0],
            lon=details["centroid"]["coordinates"][1],
            osm_id=int(details["osm_id"]),
            geom=details["geometry"] if "geometry" in details else None,
        )
        location.save()
    
    record = Record.objects.get(id=record_id)
    if record.location_set.count():
        record.location_set.all().delete()
        record.save()

    record.location_set.add(location)
    record.save()

    pass