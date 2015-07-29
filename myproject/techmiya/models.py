from django.db import models
from files import profile_image_path
from files import profile_Mainimage_path
from django.core.files.storage import FileSystemStorage


# Create your models here.

class Vehicle(models.Model):

	MAKE_CHOICES = (
		('', ''),
		('Unknown', 'Unknown'),
		('ACURA', 'ACURA'),
		('ALFA', 'ALFA'),
		('ASTON', 'ASTON'),
		('AUDI', 'AUDI'),
		('BMW', 'BMW'),
		('Leyland DAF', 'Leyland DAF'),
		('ERF', 'ERF'),
		('FIAT', 'FIAT'),
		('Foden', 'Foden'),
		('FORD', 'FORD'),
		('GOLF', 'GOLF'),
		('HONDA', 'HONDA'),
		('Hyundai', 'Hyundai'),
		('IVECO', 'IVECO'),
		('MAZDA', 'MAZDA'),
		('MERCEDES-BENZ', 'MERCEDES-BENZ'),
		('MITSUBISHI', 'MITSUBISHI'),
		('NISSAN', 'NISSAN'),
		('RENAULT', 'RENAULT'),
		('SCANIA', 'SCANIA'),
		('TOYOTA', 'TOYOTA'),
		('VOLVO', 'VOLVO')
	)#Leyland Daf | ERF | Iveco | Mercedes Benz | Volvo | Scania | Renault
	
	TYPE_CHOICES = (
		("TRUCK", "TRUCK"),
		#("4 X 4 PICKUP", "4 X 4 PICKUP"),
		#("CAR", "CAR"),
		#("TRAILER", "TRAILER"),
		("MACHINERY & EQUIPS", "MACHINERY & EQUIPMENT")
	)
	
	ref = models.CharField("Reference No (1 - 6 Characters Only)", unique=True, max_length=6)
	type = models.CharField('Type of Vehicle', max_length=50, choices = TYPE_CHOICES )
	make = models.CharField('Make', max_length=30, choices = MAKE_CHOICES, blank=True )
	model = models.CharField('Model', max_length=100)
	year = models.IntegerField("Year (E.g. 1990)", max_length=4, blank=True, null=True)
	desc = models.TextField("Description", max_length=400)
	
	SHOWROOM_CHOICES = (
		("Y", "Yes"),
		("N", "No")
	)
	
	showroom = models.CharField('In Zambia\'s Showroom', choices = SHOWROOM_CHOICES, default="N", max_length="1", blank=True)
	
	STATUS_CHOICES = (
		("A", "Available"),
		("S", "SOLD")
	)
	
	status = models.CharField('Status', choices = STATUS_CHOICES, default="A", max_length="1", blank=True)
	#short_desc = models.CharField("Long Description", max_length=400)
	date_added = models.DateField("Date Added")
	
	#ab = FileSystemStorage(location="/site_media/vehicles/")
	image = models.ImageField(upload_to="vehicle_images", null=True)
	
	class Meta:
			ordering = ["date_added"]

	#def __unicode__(self):
	#	return self.model
	
	def __str__(self):
		return "%s, %s, %s, %s, (%s) - In Showroom(%s)" % (self.type, self.year, self.make, self.model, self.ref, self.showroom)
	

class Picture(models.Model):
		model = models.ForeignKey(Vehicle)
		image = models.ImageField(upload_to="vehicle_images", null=True)

		def __str__(self):
			return '%s\'s Image' % self.model

# ---------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------#

import re
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError

# A simple contact form with four fields.
class ContactDetail(models.Model):
	
	TITLE_CHOICES = (
		('Mr', 'Mr'),
		('Miss', 'Miss'),
		('Mrs', 'Mrs'),
		('Dr', 'Dr')
	)
	title = models.CharField('Title', max_length=10, choices = TITLE_CHOICES )
	full_name = models.CharField("Full Name", max_length = 30)
	
	LOCATION_CHOICES = (
		('United Kingdom', 'United Kingdom'),
		('Zambia', 'Zambia'),
		('Namibia', 'Namibia'),
		('Congo', 'Congo'),
		('Burundi', 'Burundi'),
		('Botswana', 'Botswana'),
		('Tanzania', 'Tanzania'),
		('Malawi', 'Malawi')
	)
	
	location = models.CharField('Location', max_length="50", choices = LOCATION_CHOICES)
	
	address = models.CharField('Address (Optional)', max_length=300, blank=True)
	city = models.CharField('City/Town', max_length=300, blank=True)
	postcode = models.CharField('PostCode (Optional)', max_length=10, blank=True)
	
	
	telephone = models.CharField('Phone', max_length="20", blank=True)
	email = models.CharField('Email', max_length="100")
	
	def __str__(self):
		return "%s. %s\'s Contact Details - %s" % (self.title, self.full_name, self.location)
	
	
# ---------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------#
	
