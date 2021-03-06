import json
import os

from django.db import models
from django.db import transaction

MINERAL_DATA_SOURCE = "/assets/data/minerals.json"


class Mineral(models.Model):
    name = models.CharField(unique=True, max_length=255)
    image_filename = models.FileField(blank=True, default='')
    image_caption = models.TextField(blank=True, default='')
    category = models.CharField(blank=True, default='', max_length=255)
    formula = models.TextField(blank=True, default='', max_length=255)
    strunz_classification = models.CharField(blank=True, default='', max_length=255)
    crystal_system = models.CharField(blank=True, default='', max_length=255)
    unit_cell = models.CharField(blank=True, default='', max_length=255)
    color = models.CharField(blank=True, default='', max_length=255)
    crystal_symmetry = models.CharField(blank=True, default='', max_length=255)
    cleavage = models.CharField(blank=True, default='', max_length=255)
    mohs_scale_hardness = models.CharField(blank=True, default='', max_length=255)
    luster = models.CharField(blank=True, default='', max_length=255)
    streak = models.CharField(blank=True, default='', max_length=255)
    diaphaneity = models.CharField(blank=True, default='', max_length=255)
    optical_properties = models.CharField(blank=True, default='', max_length=255)
    group = models.CharField(blank=True, default='', max_length=255)
    refractive_index = models.CharField(blank=True, default='', max_length=255)
    crystal_habit = models.CharField(blank=True, default='', max_length=255)
    specific_gravity = models.CharField(blank=True, default='', max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def ingest_data_from_json_file(cls):
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ MINERAL_DATA_SOURCE, encoding="utf8") as source:
            json_string = source.read()
            for each in json.loads(json_string):
                each = {k.replace(' ', '_'): v for k, v in each.items()}
                mineral = Mineral(**each)
                try:
                    with transaction.atomic():
                        mineral.save()
                except Exception as e:  #Don't care.  Just put the records in there without failing.
                    print(e)
        return True
