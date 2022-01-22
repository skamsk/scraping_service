import codecs
import os
import sys



proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

import django
django.setup()
from django.db import DatabaseError
from scraping.models import City, Language, Vacancy
from scraping.parsers import *

parsers = (
    (work, 'https://www.work.ua/ru/jobs-kyiv-python/'),
)

city = City.objects.filter(slug='пермь').first()
language = Language.objects.filter(slug='python').first()

print(city)
jobs, errors = [], []

for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass

# h = codecs.open('work.txt', 'w', 'utf-8')
# h.write(str(jobs))
# h.close()