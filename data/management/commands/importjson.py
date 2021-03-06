import re
from dateparser.search import search_dates
from dateparser import parse as date_parse
from glob import iglob
from json import load as load_json
from django.core.management.base import BaseCommand
from data.models import Record, Tag
from collections import Iterable

JSONPATTERN = '/*.json'


class Command(BaseCommand):
    help = 'Import json files from folder'

    def _tag_cleanup(self, tag):
        cleantag = re.sub(r"(\ Dr)$", " Drive", tag)
        cleantag = re.sub(r"(\ Pl)$", " Place", cleantag)
        cleantag = re.sub(r"(\ St)$", " Street", cleantag)
        cleantag = re.sub(r"(\ Terr)$", " Terrace", cleantag)
        cleantag = re.sub(r"(\ Rd)$", " Road", cleantag)
        cleantag = re.sub(r"(\ Gdns)$", " Gardens", cleantag)
        cleantag = re.sub(r"(\ Ave)$", " Avenue", cleantag)
        cleantag = re.sub(r"(\ Cres)$", " Cresent", cleantag)
        cleantag = re.sub(r"(\ La)$", " Lane", cleantag)
        cleantag = re.sub(r"(\ Sq)$", " Square", cleantag)
        cleantag = re.sub(r"(\ Ct)$", " Court", cleantag)
        cleantag = re.sub(r"(\ Pl\ 3)$", " Place", cleantag)
        
        return cleantag

    def _date_cleanup(self, date_raw):
        tidy_date = re.sub(r"n\.d\. \?c\.|n\.d\. c\.|c\.", "", date_raw)
        dates = search_dates(tidy_date, settings={'PREFER_DATES_FROM': 'past'})
        if isinstance(dates, Iterable):
            ordered = sorted(dates, key=lambda date: date[1])
            date = ordered[0][1]
        else:
            date = date_parse(tidy_date)

        if date is None:
            tidy_date = re.sub("-", " ", tidy_date)[:-1]
            dates = search_dates(tidy_date, settings={'PREFER_DATES_FROM': 'past'})
            if isinstance(dates, Iterable):
                ordered = sorted(dates, key=lambda date: date[1])
                date = ordered[0][1]
            else:
                date = date_parse(tidy_date)

        return date

    def _import(self, folder):
        json_folder = folder + JSONPATTERN

        print("Nuking the DB:", end='')
        Record.objects.all().delete()
        Tag.objects.all().delete()
        print("Done")
        print("Importing: %s" % json_folder)

        file_counter = 0

        for filename in iglob(json_folder):
            with open(filename) as f:
                file_counter += 1
                print("#%s" % file_counter)

                details = load_json(f)

                record = Record(
                    record_number=details['record number'] if 'record number' in details else None,
                    area=details['area'] if 'area' in details else None,
                    date_raw=details['date'] if 'date' in details else None,
                    date=self._date_cleanup(details['date']) if 'date' in details else None,
                    street=details['street'] if 'street' in details else None,
                    number=details['number'] if 'number' in details else None,
                    image_url=details['image_url'] if 'image_url' in details else None,
                    description=details['description'] if 'description' in details else None,
                    caption=details['caption'] if 'caption' in details else None
                )
                record.save()

                if record.date is None:
                    print("Error with date in %s: %s" % (
                        details['record number'],
                        details['date'] if 'date' in details else "NO DATE"
                    ))

                if details['tags'] is not None:
                    for tag_title in details['tags']:
                        tag_title = self._tag_cleanup(tag_title)
                        try:
                            tag = Tag.objects.get(title=tag_title)
                        except Tag.DoesNotExist:
                            tag = Tag(title=tag_title)
                            tag.save()

                        record.tags.add(tag)
                        record.save()



    def add_arguments(self, parser):
        parser.add_argument('--folder', type=str)

    def handle(self, *args, **options):
        if options['folder']:
            self._import(options['folder'])
        else:
            print("Folder required: --folder")
