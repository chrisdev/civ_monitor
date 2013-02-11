from django.contrib import admin
from .models import Publication, Monthly

class MonthlyAdmin(admin.ModelAdmin):
    date_hierarchy='dateix'


class PublicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Monthly,MonthlyAdmin)
admin.site.register(Publication,PublicationAdmin)
