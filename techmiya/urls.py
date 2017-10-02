from django.conf.urls import include, url
from django.conf.urls.static import static
from techmiya.views import *
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#site_media = os.path.join(os.path.dirname(__file__), 'site_media')
urlpatterns = [
	url(r'^$', home_page),
    # Example:
    # (r'^techmiya_base/', include('techmiya_base.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', contacts),
    url(r'^stock/', stock_page),

	url(r'^vehicle/(?P<vehicle_id>\d+)/$', detail),
    
    url(r'^trucks/', stock_trucks),
    url(r'^pickups/', stock_pickups),
    url(r'^cars/', stock_cars),
    url(r'^trailers/', stock_trailers),
	#(r'^showroom/', stock_showroomAll),
	url(r'^showroom/all/', stock_showroomAll),
	url(r'^showroom/search/', stock_showroom_search),
    url(r'^machinery_and_equipments/', stock_machinery),
	url(r'^google/', google),

]
