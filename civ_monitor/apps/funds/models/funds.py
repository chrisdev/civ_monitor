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



    # def show_funds(self):
    #     return """<a href="/admin/core/fund/?issuer__id__exact=%s">
    #     <span style="color:green;font-size=large"><img src="/site_media/images/view.png" />&nbsp;View</a>""" % (self.id)

    # show_funds.allow_tags=True
    # show_funds.short_description='View Funds'

    # def last_volume_data(self):
    #     try:
    #         return self.issuervolumeaggregates_set.all().order_by('-period_ending')[0]
    #     except IndexError:
    #         return None

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

    # def is_local_currency(self):
    #     if self.currency.code == 'TTD':
    #         return True
    #     else:
    #         return False
    # is_local_currency.short_description='Local Currency'
    # is_local_currency.boolean=True

    def __unicode__(self):
        return '%s-%s' % (self.description, self.symbol)

    # def last_volume_report(self):
    #     try:
    #         obs=self.fundvolumedata_set.all().order_by('-period_ending')[0]
    #         return obs.period_ending.dateix.strftime('%Y-%m-%d')
    #     except IndexError:
    #         return '-'
    # last_volume_report.short_description='Last Volume'

    # def last_net_assets(self):
    #     pd=last_valid_pubdate()
    #     try:
    #         vd=self.fundvolumedata_set.filter(
    #             period_ending__dateix__lte=pd.dateix).order_by('-period_ending')[0]
    #         return vd.tt_total_net_assets_under_management
    #     except IndexError:
    #         return None

    # def last_nav(self):
    #     pd=last_valid_pubdate()
    #     try:
    #         vd=self.fundvolumedata_set.filter(
    #             period_ending__dateix__lte=pd.dateix).order_by('-period_ending')[0]
    #         vd=self.fundvolumedata_set.all().order_by('-period_ending')[0]
    #         return vd.unit_net_asset_value
    #     except IndexError:
    #         return None

    # def volume_reports(self):
    # return """<a href="/admin/core/fundvolumedata/?fund__id__exact=%s"><img
    # src="/media/img/admin/icon_changelink.gif">&nbsp;Edit</a>""" % (self.id)

    # volume_reports.allow_tags=True
    # volume_reports.short_description='Data'

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
