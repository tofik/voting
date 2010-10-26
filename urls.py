from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^polls/', include('polls.urls')),
                       # (r'^polls/(?P<poll_id>\d+)/$', 'details'),
                       # (r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
                       # (r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
                       (r'^admin/', include(admin.site.urls)),
                       )
