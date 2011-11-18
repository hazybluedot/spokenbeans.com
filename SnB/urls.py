from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SnB.views.home', name='home'),
    # url(r'^SnB/', include('SnB.foo.urls')),
    url(r'^roastorder/', 'SnB.records.views.current_roast_order'),
    url(r'^order.html', 'SnB.records.views.order_form'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'', include('SnB.records.urls')),
)

