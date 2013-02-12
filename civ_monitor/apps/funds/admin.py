from django.contrib import admin
from .models import (InternationalClassification, LegalStatus,
                     FundScheme, Issuer, Fund, ActiveStatus
                     )


class InternationalClassificationAdmin(admin.ModelAdmin):
    pass


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

    def fund_count(self, obj):
        return obj.funds.count()
    fund_count.short_description = 'No. Funds'

    def show_funds(self, obj):
        return """<a href="/admin/core/fund/?issuer__id__exact=%s">
        <span style="color:green;font-size=large"><img src="/site_media/images/view.png" />&nbsp;View</a>""" % (obj.id)

    show_funds.allow_tags = True
    show_funds.short_description = 'View Funds'


admin.site.register(InternationalClassification,
                    InternationalClassificationAdmin)

admin.site.register(Issuer, IssuerAdmin)
