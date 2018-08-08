import re
from glob import iglob
import json
from django.core.management.base import BaseCommand
from collections import Iterable
from data.models import Location, Record

JSONPATTERN = '/*.json'


class Command(BaseCommand):
    help = 'Import and merge location data from folder'

    def _file_to_record_number(self, folder, filename):
        record = re.sub(folder, "", filename)
        record = re.sub("/", "", record)
        record = re.sub(".json", "", record)
        return record

    def _import(self, folder):
        json_folder = folder + JSONPATTERN

        print("Nuking locations:", end='')
        Location.objects.all().delete()
        print("Done")
        print("Importing: %s" % json_folder)

        file_counter = 0

        for filename in iglob(json_folder):
            with open(filename) as f:
                file_counter += 1
                record_id = self._file_to_record_number(folder, filename)
                print("[%04d] %s " % (
                    file_counter,
                    record_id
                ), end="")
                details = json.load(f)[0]

                try:
                    location = Location.objects.get(place_id=int(details["place_id"]))
                    print("loaded ", end="")
                
                except Location.DoesNotExist:
                    location = Location(
                        place_id=int(details["place_id"]),
                        display_name=details["display_name"],
                        lat=float(details["lat"]),
                        lon=float(details["lon"]),
                        osm_id=int(details["osm_id"]),
                        geom=details["geojson"] if "geojson" in details else None,
                    )
                    location.save()
                    print("saved ", end="")

                # Synching with record
                try:
                    record = Record.objects.get(record_number=record_id)
                    location.records.add(record)
                    location.save()
                    print("linked ", end="")

                except Record.DoesNotExist:
                    print("record missing")
                    location.delete()

                print("")


    def add_arguments(self, parser):
        parser.add_argument('--folder', type=str)

    def handle(self, *args, **options):
        if options['folder']:
            self._import(options['folder'])
        else:
            print("Folder required: --folder")
