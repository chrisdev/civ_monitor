from django.db import models
from .funds import Fund, Issuer
from django_countries import CountryField
from filer.fields.image import FilerImageField
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from model_utils import Choices
from model_utils.fields import StatusField


class OfficerDirector(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    country = CountryField(blank=True)
    photo = FilerImageField(null=True, blank=True)
    legacy_id = models.IntegerField(editable=False, null=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name_plural = "Officers/Directors"
        app_label = 'funds'


class ServiceManager(models.Model):
    name = models.CharField(max_length=150)
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=50, blank=True,)
    fax = models.CharField(max_length=50, blank=True)
    country = CountryField()
    website = models.URLField(blank=True)
    legacy_id = models.IntegerField(editable=False, null=True)

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        ordering = ('name', 'country')
        app_label = 'funds'


class FundServiceManager(models.Model):
    STATUS = Choices('active', 'suspended', 'other')
    fund = models.ForeignKey(Fund, related_name='service_manager')
    service_manager = models.ForeignKey(ServiceManager)
    position = models.CharField(max_length=50, blank=True)
    effective_date = models.DateField(null=True, blank=True)
    status = StatusField(default=STATUS.active)
    notes = models.TextField(blank=True)
    updated_by = models.ForeignKey(User, null=True, editable=False)

    def __unicode__(self):
        return "%s-%s-%s-%s-%s" % (
            self.service_manager,
            self.fund,
            self.effective_date,
            self.position,
            self.status
        )

    class Meta:
        ordering = ('fund', 'service_manager',)
        order_with_respect_to = 'fund'
        app_label = 'funds'


class FundOfficer(models.Model):
    STATUS = Choices('active', 'suspended', 'other')
    fund = models.ForeignKey(Fund, related_name='fund_officers')
    officer = models.ForeignKey(OfficerDirector)
    position = models.CharField(max_length=50, blank=True)
    effective_date = models.DateField(null=True, blank=True)
    status = StatusField(default=STATUS.active)
    notes = models.TextField(blank=True)
    updated_by = models.ForeignKey(User, null=True, editable=False)

    def __unicode__(self):
        return "%s-%s-%s" % (self.officer, self.fund, self.position)

    class Meta:
        ordering = ('fund',)
        order_with_respect_to = 'fund'
        app_label = 'funds'


class IssuerOfficer(models.Model):
    STATUS = Choices('active', 'suspended', 'other')
    issuer = models.ForeignKey(Issuer, related_name='issuer_officers')
    officer = models.ForeignKey(OfficerDirector)
    position = models.CharField(max_length=50, blank=True)
    effective_date = models.DateField(null=True, blank=True)
    status = StatusField(default=STATUS.active)
    notes = models.TextField(blank=True)
    updated_by = models.ForeignKey(User, null=True, editable=False)

    def __unicode__(self):
        return "%s-%s-%s" % (self.officer, self.issuer, self.position)

    class Meta:
        ordering = ('issuer',)
        order_with_respect_to = 'issuer'
        unique_together = ("officer", "issuer")
        app_label = 'funds'
