from django.conf.urls.defaults import *
from myproject.techmiya.views import *
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#site_media = os.path.join(os.path.dirname(__file__), 'site_media')
urlpatterns = patterns('',		
	(r'^$', home_page),
    # Example:
    # (r'^techmiya_base/', include('techmiya_base.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^contact/', contacts),
    (r'^stock/', stock_page),

	(r'^vehicle/(?P<vehicle_id>\d+)/$', detail),
    
    (r'^trucks/', stock_trucks),
    (r'^pickups/', stock_pickups),
    (r'^cars/', stock_cars),
    (r'^trailers/', stock_trailers),
	#(r'^showroom/', stock_showroomAll),
	(r'^showroom/all/', stock_showroomAll),
	(r'^showroom/search/', stock_showroom_search),
    (r'^machinery_and_equipments/', stock_machinery),
	(r'^google/', google),

)
