from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^index', 'data.views.index'),
	(r'^api/listing', 'data.views.create'),
	(r'^api/listing/$', 'data.views.update'),
	(r'^api/stats/search', 'data.views.getStats'),
	(r'^api/search', 'data.views.getExact'),
    # Examples:
    # url(r'^$', 'craigslist.views.home', name='home'),
    # url(r'^craigslist/', include('craigslist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
