from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=4)
    description = models.CharField(max_length=100)
    numcode = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Currency Codes'
        ordering = ('code',)
