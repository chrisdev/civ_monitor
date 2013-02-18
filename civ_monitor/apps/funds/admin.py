from django.contrib import admin
from .models import (InternationalClassification, LegalStatus,
                     FundScheme, Issuer, Fund, ActiveStatus,
                     FundServiceManager, OfficerDirector,
                     ServiceManager, FundOfficer, IssuerOfficer,
                     VolumeReportSubmission, FundVolumeData
                     )
from publications.models import Monthly
from django.contrib.admin import SimpleListFilter
from django.contrib.humanize.templatetags.humanize import intcomma
from django.contrib import messages
import xlrd
from os.path import basename
from datetime import datetime

FILE_LAYOUT = {
    'VR060': 'total_units_sold',
    'VR070': 'total_units_redeemed',
    'VR080': 'total_unit_holders',
    'VR090': 'total_units_issued_outstanding',
    'VR100': 'tt_value_sales',
    'VR110': 'tt_value_redemptions',
    'VR120': 'unit_net_asset_value',
    'VR130': 'tt_total_net_assets_under_management'
}

ERROR_TYPES = {
    1: 'Invalid Series found on Worksheet',
    2: 'Not a valid Excel file',
    3: 'Submitted file contains no valid wook sheets',
    4: 'Invalid Fund code for this issuer',
    5: 'Could not find valid reporting date',
    6: 'Invalid series name',
    7: 'No value found for this series',
    8: 'Key series contain no data',
    9: 'Invalid Fund Name',
}


class InternationalClassificationAdmin(admin.ModelAdmin):
    pass


class OfficerDirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'telephone', 'email',)
    search_fields = ('first_name', 'last_name', 'email',)


class ServiceManagerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', ]
    search_fields = ['name', 'country', ]


class FundServiceManagerInline(admin.TabularInline):
    model = FundServiceManager
    extra = 3


class FundOfficerInLine(admin.TabularInline):
    model = FundOfficer
    extra = 3


class IssuerOfficerInline(admin.TabularInline):
    model = IssuerOfficer
    extra = 3


class FundServiceManagerAdmin(admin.ModelAdmin):
    list_display = ('fund', 'position', 'active',)
    search_fields = ('position', 'fund',)


class IssuerAdmin(admin.ModelAdmin):

    list_display = ('name', 'symbol', 'fund_count', 'show_funds')
    list_filter = ('is_local_entity',)
    search_fields = ('symbol', 'name',)
    fieldsets = (
        (None, {'fields': ('name', 'symbol', 'is_local_entity',
                'address_1', 'address_2', 'country', 'fax', 'telephone')
                }
         ),
        ('Optional Data', {'fields': ('email', 'website'),
                           'classes': ('collapse',)
                           }
         ),
    )

    inlines = [
        IssuerOfficerInline
    ]

    def fund_count(self, obj):
        return obj.funds.count()
    fund_count.short_description = 'No. Funds'

    def show_funds(self, obj):
        tmpl = (
            '<div class="link-tools">'
            '<a href="/admin/core/fund/?issuer__id__exact=%s" class="golink">'
            'Show Funds</a>'
            '</div>'
        )
        return tmpl % (obj.id)

    show_funds.allow_tags = True
    show_funds.short_description = ''


class LocalCurrencyFilter(SimpleListFilter):
    title = 'currency denomination'

    parameter_name = 'currency'

    def lookups(self, request, model_admin):

        return (
            ('local', 'Local currency'),
            ('foreign', 'Foreign currency')
        )

    def queryset(self, request, queryset):
        if self.value() == 'local':
            return queryset.filter(currency__code='TTD')
        if self.value() == 'foreign':
            return queryset.exclude(currency__code='TTD')


class FundAdmin(admin.ModelAdmin):
    list_display = (
        'symbol',
        'description',
        'current_activity_status',
        'issuer',
        'last_data_submission',
        'show_volume_reports'
    )

    list_filter = ('fund_scheme', 'issuer', LocalCurrencyFilter)

    search_fields = (
        'issuer__name', 'issuer__symbol', 'symbol',
        'description',
    )

    ordering = ['symbol']

    def current_activity_status(self, obj):
        return obj.get_activity_status()

    current_activity_status.short_description = 'Active'
    current_activity_status.boolean = True

    def show_volume_reports(self, obj):
        tmpl = (
            '<div class="link-tools">'
            '<a href="/admin/funds/fundvolumedata/?fund__id__exact=%s" '
            'class="golink">'
            'Show Volume Reports</a>'
            '</div>'
        )

        return tmpl % (obj.id)

    show_volume_reports.allow_tags = True
    show_volume_reports.short_description = ''

    def last_data_submission(self, obj):
        try:
            obs = obj.volumedata.all().order_by('-period_ending')[0]
            return "{} [by {} on {}] )".format(
                obs.period_ending.dateix.strftime('%Y-%m'),
                obs.user,
                obs.modified.strftime('%Y-%m-%d: %H')

            )
        except IndexError:
            return '-'

    last_data_submission.short_description = 'last Submission'

    def last_net_assets(self, obj):
        return '-'
        # pd=last_valid_pubdate()
        # try:
        #     vd=self.fundvolumedata_set.filter(
        #         period_ending__dateix__lte=pd.dateix).order_by('-period_ending')[0]
        #     return vd.tt_total_net_assets_under_management
        # except IndexError:
        #     return None

    def last_nav(self, obj):
        return '-'
        # pd=last_valid_pubdate()
        # try:
        #     vd=self.fundvolumedata_set.filter(
        #         period_ending__dateix__lte=pd.dateix).order_by('-period_ending')[0]
        #     vd=self.fundvolumedata_set.all().order_by('-period_ending')[0]
        #     return vd.unit_net_asset_value
        # except IndexError:
        #     return None

    inlines = [
        FundServiceManagerInline,
        FundOfficerInLine
    ]


class FundVolumeDataAdmin(admin.ModelAdmin):

    list_display = [
        'get_fund_symbol',
        'period_ending',
        'tt_net_assets_under_man_fmt',
        'tt_value_sales_fmt',
        'tt_value_redemptions_fmt',
        'unit_net_asset_value',
    ]

    search_fields = ['fund__symbol', 'fund__issuer__symbol',
                     'fund__issuer__name',
                     'period_ending__dateix']
    fieldsets = (
        (None, {'fields': (
            'fund',
            'period_ending'
        )}
        ),
        ('Volume Data:', {
         'classes': ('wide', 'extrapretty'),
         'fields': (
             'total_units_sold',
             'total_units_redeemed',
             'total_units_issued_outstanding',
             'total_unit_holders',
             'tt_value_redemptions',
             'tt_value_sales',
             'unit_net_asset_value',
             'tt_total_net_assets_under_management',
             'is_estimated',
             'is_valid'
         ),
         }
         )
    )

    def get_fund_symbol(self, obj):
        return obj.fund.symbol

    get_fund_symbol.short_description = 'Fund'

    def tt_net_assets_under_man_fmt(self, obj):
        return '-' if obj is None else intcomma(
            round(obj.tt_total_net_assets_under_management, 2)
        )
    tt_net_assets_under_man_fmt.short_description = 'Assets Under Management'

    def tt_value_sales_fmt(self, obj):
        return '-' if obj is None else intcomma(
            round(obj.tt_value_sales, 2)
        )
    tt_value_sales_fmt.short_description = 'Sales'

    def tt_value_redemptions_fmt(self, obj):
        return '-' if obj is None else intcomma(
            round(obj.tt_value_redemptions, 2)
        )
    tt_value_redemptions_fmt.short_description = 'Redemptions'

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def process_file(self):
        # if not is_file(self.filepath.path):
        # messages.error(request, 'Invalid File!!')
        return


class XlLoader(object):

    STATUS_CODES = [
        'clean',
        'warnings',
        'failed'
    ]

    def __init__(self, request, obj):

        self.STATUS = 'clean'
        self.submission = obj
        self.request = request
        self.exceptions = []
        self.funds_processed = []
        messages.set_level(request, messages.WARNING)
        try:
            self.workbook = xlrd.open_workbook(obj.filepath.path)
        except (IOError, NameError, xlrd.XLRDError):
            messages.add_message(request,
                                 messages.ERROR,
                                 "invalid or courupt file {}".format(
                                     basename(obj.filepath.name))
                                 )
            return False

        for sh in self.workbook.sheets():
            self.process_sheet(sh)

        print self.funds_processed
        print self.exceptions
        # write some mesages
        # import ipdb; ipdb.set_trace()

        messages.add_message(
            request,
            messages.WARNING,
            "{} funds processed including:".format(
            len(self.funds_processed))
        )

        for r in self.funds_processed:
            messages.add_message(
                request,
                messages.WARNING,
                " {} - {} ".format(r[0], r[1])

            )

        for e in self.exceptions:
            error_num = e[0]
            error_type_txt = ERROR_TYPES[e[0]]
            wksheet = e[1]
            error_fld = e[2]
            msg = "(%s) worksheet[%s] - %s %s " % (error_num,
                                                   wksheet,
                                                   error_type_txt,
                                                   error_fld)

            messages.add_message(
                request,
                messages.ERROR,
                msg
            )

    def process_sheet(self, sheet):
        rows = list(self.get_rows(sheet))
        # import ipdb
        # ipdb.set_trace()
        period_ending = self.__get_period_ending(rows, sheet)
        if period_ending is None:
            self.exceptions.append([5, sheet.name, None])
            return
        fund = self.__get_fund(rows)
        if not fund:
            self.exceptions.append([9, sheet.name, "not found"])
            return
        data = self.__get_data(rows)
        self.__load_data(period_ending, fund, data, sheet)

    def __get_data(self, rows):
        data = {}
        for i in range(len(rows)):
            try:
                dkey = FILE_LAYOUT[rows[i][0].value]
                dvalue = rows[i][3].value
                try:
                    data[dkey] = float(dvalue)
                except ValueError:
                    data[dkey] = 0.0
            except KeyError:
                continue
        return data

    def __get_value(self, data, key):
        try:
            value = data[FILE_LAYOUT[key]]
        except KeyError:
            self.exceptions.append([6, self.current_sheet, key])
            value = None
        if not value:
            self.exceptions.append([7, self.current_sheet, FILE_LAYOUT[key]])
            return 0.0
        return value

    def __load_data(self, period_ending, fund, data, sheet):
        # import ipdb;ipdb.set_trace()

        obj, created = FundVolumeData.objects.get_or_create(
            fund=fund,
            period_ending=period_ending,
            defaults=data
        )
        self.funds_processed.append([fund, period_ending])
        if not data.get('tt_total_net_assets_under_management'):
            messg = "%s %s" % (fund.symbol,
                               'VR130-Total Assets Under Management'
                               )
            self.exceptions.append([8, sheet.name, messg])
        if not data.get('total_units_issued_outstanding'):
            messg = "%s %s" % (fund.symbol,
                               'VR90- Total units/shares issued and outstandig'
                               )
            self.exceptions.append([8, sheet.name, messg])

    def __get_fund(self, rows):
        for i in range(len(rows)):
            if rows[i][0].value == 'VR040':
                try:
                    return Fund.objects.get(
                        symbol=rows[i][2].value,
                        issuer=self.submission.issuer)
                except Fund.DoesNotExist:
                    return

    def __get_period_ending(self, rows, sheet):
        for i in range(len(rows)):
            if rows[i][0].value == 'VR010':
                rt, value = (sheet.row_types(i)[2],
                             sheet.row_values(i)[2]
                             )
                if rt != 3:
                    return

                dt = xlrd.xldate_as_tuple(value, self.workbook.datemode)

                try:
                    return Monthly.objects.get(
                        dateix__year=dt[0],
                        dateix__month=dt[1],
                        dateix__day=dt[2]
                    )
                except Monthly.DoesNotExist:
                    return

    def get_rows(self, sheet):
        for i in range(sheet.nrows):
            yield sheet.row(i)


class VolumeReportSubmissionAdmin(admin.ModelAdmin):

    # def has_change_permission(self, request, obj=None):
    #     return False  # To remove the 'Save and continue editing' button

    def save_model(self, request, obj, form, change):
        # import ipdb; ipdb.set_trace()
        obj.user = request.user
        obj.save()
        self.process_file(request, obj)

    def process_file(self, request, obj):
        XlLoader(request, obj)


admin.site.register(InternationalClassification,
                    InternationalClassificationAdmin)
admin.site.register(Issuer, IssuerAdmin)
admin.site.register(Fund, FundAdmin)
admin.site.register(OfficerDirector, OfficerDirectorAdmin)
admin.site.register(ServiceManager, ServiceManagerAdmin)
admin.site.register(FundVolumeData, FundVolumeDataAdmin)
admin.site.register(VolumeReportSubmission, VolumeReportSubmissionAdmin)
