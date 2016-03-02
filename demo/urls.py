from django.conf.urls import patterns, include, url
from demo_strbd import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),t
    # url(r'^blog/', include('blog.urls')),
    url('^login/',include('login.urls')),
    url(r'^cost/$',views.costView, name="cost"),
    url(r'^cost/',include('demo_strbd.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
