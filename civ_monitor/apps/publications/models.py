from django.db import models

# Create your models here.


class Monthly(models.Model):

    dateix = models.DateField(unique=True)
    legacy_id = models.IntegerField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return u'{}'.format(self.dateix.strftime('%Y-%b'))

    class Meta:
        ordering = ['dateix']
        verbose_name_plural = 'Monthly'


class Publication(models.Model):
    """
    use this to set the last valid date
    """
    CHOICES = (
        ('1', 'Provisional'),
        ('2', 'Revised'),
        ('3', 'Final')
    )
    data_status = models.CharField(choices=CHOICES, max_length=2)
    date_stamp = models.DateField(auto_now_add=True)
    data_collection_period = models.ForeignKey(
        Monthly,
        unique=True,
        limit_choices_to={'dateix__gte': '2007-12-31'}
    )

    def __unicode__(self):
        return u'Satus %s Date %s' % (
            self.data_status,
            self.data_collection_period.dateix.strftime('%Y-%b')
        )

    class Meta:
        ordering = ['-data_collection_period']
        verbose_name = 'Last valid date for Publication'
        verbose_name_plural = 'Last valid date for Publication'

