from django.db import models
from django_countries import CountryField
from utils.models import Currency
from django.contrib.auth.models import User
# Create your models here.


class InternationalClassification(models.Model):
    code = models.CharField(max_length=4, unique=True)
    description = models.CharField(max_length=300)
    fund_type = models.IntegerField()
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s-%s" % (self.code, self.name)

    class Meta:
        verbose_name_plural = 'International Classification'
        app_label = 'funds'


class LegalStatus(models.Model):
    code  = models.CharField(max_length=5)
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Legal Status'
        app_label = 'funds'


class FundScheme(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Fund Classification'
        app_label = 'funds'


class Issuer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    symbol = models.CharField(max_length=5)
    active = models.BooleanField()
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    fax = models.CharField(blank=True, max_length=50)
    telephone = models.CharField(blank=True, max_length=50)
    country = CountryField()
    is_local_entity = models.BooleanField()
    legacy_id = models.IntegerField(editable=False, null=True)

    def __unicode__(self):
        return "%s-%s" % (self.symbol, self.name)


    class Meta:
        ordering = ('name', 'symbol')
        app_label = 'funds'


class Fund(models.Model):
    issuer = models.ForeignKey(Issuer, related_name='funds')
    symbol = models.CharField(max_length=15, unique=True)
    description = models.CharField(max_length=100)
    country = CountryField()
    currency = models.ForeignKey(Currency)
    fund_scheme = models.ForeignKey(FundScheme)
    registration_date = models.DateField()
    fund_classification = models.ForeignKey(InternationalClassification)
    legal = models.ForeignKey(LegalStatus)
    open_ended = models.BooleanField()
    notes = models.TextField(null=True, blank=True)
    legacy_id = models.IntegerField(editable=False, null=True)


    def __unicode__(self):
        return '%s-%s' % (self.description, self.symbol)

    def get_latest_activity_status(self):
        try:
            return self.revisions.exclude(
                published=None).order_by("-date")[0].status
        except IndexError:
            return None

    class Meta:
        ordering = ['description']
        order_with_respect_to = 'issuer'
        app_label = 'funds'


class ActiveStatus(models.Model):
    fund = models.ForeignKey(Fund, related_name='activity_status')
    date = models.DateField()
    status = models.NullBooleanField()
    updated_by = models.ForeignKey(User)
    notes = models.CharField(blank=True, max_length=50)

    def __unicode__(self):
        if self.status is None:
            status = "Unknown"
        elif self.status:
            status = "Active"
        else:
            status = "Suspended"
        return u"{} {} {}".format(self.fund, self.date, status)

    class Meta:
        app_label = 'funds'
