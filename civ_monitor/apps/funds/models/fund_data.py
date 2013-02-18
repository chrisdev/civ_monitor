from django.db import models
from .funds import Fund, Issuer
from publications.models import Monthly
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from model_utils import Choices
from os.path import basename, isfile
from django.contrib import messages

FILE_LAYOUT = {
   'VR060':'total_units_sold',
   'VR070':'total_units_redeemed',
   'VR080':'total_unit_holders',
   'VR090':'total_units_issued_outstanding',
   'VR100':'tt_value_sales',
   'VR110':'tt_value_redemptions',
   'VR120':'unit_net_asset_value',
   'VR130':'tt_total_net_assets_under_management'
}

class VolumeReportSubmission(TimeStampedModel):

    issuer = models.ForeignKey(Issuer)
    uploaded_by = models.ForeignKey(User, null=True, editable=False)
    filepath = models.FileField(
        upload_to='data/%Y/%b',
        verbose_name='Upload Volume Report File',
        help_text=('Browse your computer to select a the '
                   'Excel file with the volume report submission:'
                   )
    )

    data_period = models.ForeignKey(
        Monthly,
        limit_choices_to={'dateix__gte': '2012-01-31'}
    )

    def __unicode__(self):
        return  '%s %s [%s]' % (
            self.issuer,
            basename(self.filepath.name),
            self.data_period.dateix.strftime('%Y-%b')
        )

    # def save(self, *args, **kwargs):
    #     super(VolumeReportSubmission, self).save(*args, **kwargs)
    #     self.process_file()



    class Meta:
        verbose_name = 'Volume Report Submission'
        verbose_name = 'Upload Volume Report File'
        app_label = 'funds'


class VolumeReportSubmissionLog(TimeStampedModel):
    volume_report_submission = models.ForeignKey(
        VolumeReportSubmission,
        related_name='volume_report_submission'
    )

    STATUS = Choices('passed', 'warnings', 'failed')

    status = models.CharField(choices=STATUS,
                              default=STATUS.passed,
                              max_length=20
                              )

    status_message = models.TextField()

    def __unicode__(self):
        return '%s - %s - %s' % (
            self.volume_report_submission,
            self.status,
            self.modified
        )

    class Meta:
        app_label = 'funds'


class FundVolumeData(TimeStampedModel):

    fund = models.ForeignKey(Fund, related_name='volumedata')
    user = models.ForeignKey(User, blank=True, null=True, editable=False)

    period_ending = models.ForeignKey(
        Monthly,
        verbose_name="Reporting Period",
        limit_choices_to={'dateix__gte': '2006-12-31'}
    )
    units_purchased_individuals = models.FloatField(
        "Individuals",
        blank=True,
        null=True
    )
    units_purchased_institutions = models.FloatField(
        "Instutions",
        blank=True,
        null=True
    )
    units_sold_agents = models.FloatField(
        verbose_name="Agents",
        blank=True,
        null=True
    )

    units_sold_inhouse = models.FloatField(
        verbose_name="In House",
        blank=True,
        null=True
    )

    units_redeemed_individuals = models.FloatField(
        verbose_name="Individuals",
        blank=True,
        null=True
    )

    units_redeemed_institutions = models.FloatField(
        verbose_name="Institutions",
        blank=True,
        null=True)

    total_units_issued_outstanding = models.FloatField(
        verbose_name="Units Issued/Outstanding",
        blank=True,
        null=True
    )

    total_unit_holders = models.FloatField(
        verbose_name="No. Unit holders",
        blank=True,
        null=True
    )

    value_units_purchased_individuals = models.DecimalField(
        verbose_name="Purchased by Individuals",
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True
    )

    value_units_purchased_institutions = models.DecimalField(
        verbose_name="Purchased by Institutions",
        max_digits=12,
        decimal_places=2,
        null=True, blank=True
    )
    value_unit_sales_agents = models.DecimalField(
        verbose_name="Sales by Agents",
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    value_unit_sales_inhouse = models.DecimalField(
        verbose_name="Sales In House",
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    value_redeemed_individuals = models.DecimalField(
        verbose_name="Redeemed by individuals",
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    value_redeemed_institutions = models.DecimalField(
        verbose_name="Redeemed by Individuals",
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    total_net_assets_under_management = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True
    )

    tt_value_units_purchased_individuals = models.FloatField(
        verbose_name="TT Purchased by Individuals",
        blank=True, null=True
    )
    tt_value_units_purchased_institutions = models.DecimalField(
        verbose_name="TT Purchased by Institutions",
        null=True,
        blank=True
    )
    tt_value_unit_sales_agents = models.DecimalField(
        verbose_name="TT Sales by Agents",
        null=True,
        blank=True
    )
    tt_value_unit_sales_inhouse = models.DecimalField(
        verbose_name="TT Sales In House",
        null=True,
        blank=True
    )
    tt_value_redeemed_individuals = models.DecimalField(
        verbose_name="TT Redeemed by Individuals",
        null=True,
        blank=True
    )
    tt_value_redeemed_institutions = models.DecimalField(
        verbose_name="TT Redeemed by Institutions",
        max_digits=12,
        decimal_places=2,
        null=True, blank=True
    )
    tt_total_net_assets_under_management = models.FloatField(
        null=True,
        blank=True
    )

    unit_net_asset_value = models.FloatField(
        verbose_name="Unit NAV",
        null=True,
        blank=True
    )

    tt_value_units_purchased_individuals = models.FloatField(
        null=True,
        default=0.0,
        blank=True
    )
    tt_value_units_purchased_institutions = models.FloatField(
        null=True,
        default=0.0,
        blank=True
    )
    tt_value_unit_sales_agents = models.FloatField(null=True,
                                                   default=0.0,
                                                   blank=True
                                                   )
    tt_value_unit_sales_inhouse = models.FloatField(null=True,
                                                    default=0.0,
                                                    blank=True
                                                    )
    tt_value_redeemed_individuals = models.FloatField(null=True,
                                                      default=0.0,
                                                      blank=True
                                                      )
    tt_value_redeemed_institutions = models.FloatField(null=True,
                                                       default=0.0,
                                                       blank=True
                                                       )
    tt_value_redemptions = models.FloatField(
        verbose_name="Redemptions ($TT)",
        null=True,
        default=0.0,
        blank=True
    )

    tt_value_sales = models.FloatField(
        verbose_name="Sales ($TT)",
        null=True,
        default=0.0,
        blank=True
    )

    tt_total_net_assets_under_management = models.FloatField(
        verbose_name="Assets Under Management ($TT)",
        null=True,
        default=0.0,
        blank=True
    )

    total_units_sold = models.FloatField(
        verbose_name="No. Units Sold",
        null=True,
        default=0.0,
        blank=True
    )

    total_units_redeemed = models.FloatField(
        verbose_name="No, Units Reedeemd",
        null=True,
        default=0.0,
        blank=True
    )

    is_estimated = models.NullBooleanField(
        verbose_name='Values Have been Estimated',
        blank=True,
        default=False
    )

    is_valid = models.NullBooleanField(
        verbose_name='Values Checked and Passed',
        blank=True,
        default=False
    )

    class Meta:
        verbose_name_plural = "Volume Data"
        order_with_respect_to = 'period_ending'
        unique_together = ('fund', 'period_ending')
        app_label = 'funds'

    def __unicode__(self):
        return "%s-%s" % (self.fund, self.period_ending)
