from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^pacotes$', hello.views.london_design, name='pacotes'),
    url(r'^london_design$', hello.views.london_design, name='london_design'),
    url(r'^parceiros$', hello.views.parceiros, name='parceiros'),
    url(r'^contact$', hello.views.contact, name='contact'),
    url(r'^contact_tour$', hello.views.contact_tour, name='contact_tour'),

    url(r'^admin/', include(admin.site.urls)),
]
