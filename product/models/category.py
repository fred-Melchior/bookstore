from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    id = models.IntegerField(max_length=25)

    def __unicode__(self):
        return self.title