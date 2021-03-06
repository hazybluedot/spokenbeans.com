from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SnB.views.home', name='home'),
    # url(r'^SnB/', include('SnB.foo.urls')),
    url(r'^$', 'SnB.views.home', name='home'),
    url(r'^index.html', 'SnB.views.home', name='home'),
    url(r'^roastorder/', 'SnB.records.views.current_roast_order'),
    url(r'^thanks.html$', 'SnB.records.views.thanks'),
    url(r'^origins.html$', 'SnB.coffee.views.origins'),
    url(r'^order.html', 'SnB.records.views.order_form'),
    url(r'^mailtest$','SnB.records.views.mail_test'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'', include('SnB.records.urls')),
)

