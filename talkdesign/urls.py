from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^pacotes', hello.views.pacotes, name='pacotes'),
    url(r'^london_design', hello.views.london_design, name='london_design'),
    url(r'^admin/', include(admin.site.urls)),
]
