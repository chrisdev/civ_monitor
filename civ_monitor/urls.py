from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

handler500 = "utils.views.server_error"

class HomePageView(TemplateView):
    template_name = "homepage.html"

urlpatterns = patterns("",
    url(r"^$",
        HomePageView.as_view(),
        name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),



)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
