import random
import string
from django.db import models

#"TD110 15-50 start"
# Create your models here.

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class KirrURL(models.Model):
    url = models.CharField(max_length = 220,)
    shortcode =  models.CharField(max_length = 15, unique = True,)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #shortcode =  models.CharField(max_length = 15, null = true,)

    def save(self, *args, **kwargs):
        self.shortcode=code_generator()
        super (KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
