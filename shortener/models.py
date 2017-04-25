from django.db import models

# Create your models here.

class KirrURL(models.Model):
    url = models.CharField(max_length = 220,)
    shortcode =  models.CharField(max_length = 15, unique = True,)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #shortcode =  models.CharField(max_length = 15, null = true,)

    def save(self, *args, **kwargs):
        super (KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
