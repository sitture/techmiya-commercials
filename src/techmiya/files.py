import random, string
from django.contrib.contenttypes.models import ContentType

def profile_image_path(image, filename):
	dir = "/site_media/vehicles/%s/vehilce_images/%s" % (image.model, filename)
	return dir
	
def profile_Mainimage_path(image, filename):
	dir = "/site_media/vehicles/%s/vehilce_images/%s" % (image, filename)
	return dir
