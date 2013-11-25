from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ras import views


admin.autodiscover()

urlpatterns = patterns('',
                       ('^$', views.base),
                       ('^date/$', views.current_datetime),
                       ('^time_rem/$', views.hours_remaning),
                       ('^search/$', views.search),
                       ('^catalog/$', views.catalog),
                       ('^catalogcalc/$', views.catalogcalc),
                       ('^contact/$', views.contact),
                       ('^save/$', views.excel_out),


         # Examples:
         # url(r'^$', 'Calculation.views.home', name='home'),
         # url(r'^Calculation/', include('Calculation.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

