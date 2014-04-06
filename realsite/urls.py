from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'realsite.views.home', name='home'),
    # url(r'^blog/', inclu
    url(r'^planner/', include('planner.urls', namespace='planner')),
    url(r'^admin/', include(admin.site.urls)),
)
