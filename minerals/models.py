import json
import os

from django.db import models

MINERAL_DATA_SOURCE = "/assets/data/minerals.json"

class Mineral(models.Model):
    name = models.CharField(max_length=255)
    image_filename = models.FileField()
    image_caption = models.TextField()
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

    def __str__(self):
        return self.title

    @classmethod
    def ingest_data_from_json_file(cls):
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ MINERAL_DATA_SOURCE, encoding="utf8") as source:
            json_string = source.read()
            for each in json.loads(json_string):
                print(each)


