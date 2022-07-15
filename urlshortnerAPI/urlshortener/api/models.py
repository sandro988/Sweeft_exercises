from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import random
import string

# Create your models here.
class Link(models.Model):
    long_url = models.URLField(max_length=250, blank=False)
    short_url = models.CharField(max_length=10, unique=True)
    visit_count = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url 

    def visit_count_increment(self):
        self.visit_count += 1
        self.save()
