from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tracker.views import all_countries

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pop_tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', all_countries),
)
