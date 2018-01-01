from django.db import models
from django.utils.timezone import now

# Create your models here.

class ATI(models.Model):
    orgname_en = models.CharField(max_length=150)
    orgname_fr = models.CharField(max_length=150)
    year = models.CharField(max_length=4, blank=True)
    month = models.CharField(max_length=4, blank=True, help_text="Enter number 1 to 12")
    desc_en = models.TextField(blank=True, null=True)
    desc_fr = models.TextField(blank=True, null=True)
    request_no = models.CharField(max_length=150, verbose_name="Identifier")

    def __str__(self):
        return "{}".format(self.request_no)

    def save(self, *args, **kwargs):

        super(ATI, self).save(*args, **kwargs)

