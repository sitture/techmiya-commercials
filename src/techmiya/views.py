# Create your views here.
from django import forms
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response
#from babylon.forms import *

from .models import *

from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from django.views.decorators.csrf import csrf_exempt

# ---------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------#

def home_page(request):
    return render_to_response('main_page.html', RequestContext(request))

def google(request):
	return render_to_response('googleee-db8bd5bbd4254.html', RequestContext(request))
# ---------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------#

def contactview(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['haroon_sheikh@hotmail.co.uk'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thankyou/')
    else:
        return render_to_response('contacts.html', {'form': ContactForm()})
    return render_to_response('contacts.html', {'form': ContactForm()},
        RequestContext(request))
# ---------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------#

def stock_page(request):
    return render_to_response('stock.html', RequestContext(request))

# ---------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------#
#Leyland Daf | ERF | Iveco | Mercedes Benz | Volvo | Scania | Renault

def stock_trucks(request):
	blank_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make=""))
	daf_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="Leyland DAF"))
	erf_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="ERF"))
	iveco_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="IVECO"))
	merc_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="MERCEDES-BENZ"))
	volvo_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="VOLVO"))
	foden_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="Foden"))
	scania_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="SCANIA"))
	renault_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="RENAULT"))
	
	acura_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="ACURA"))
	golf_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="GOLF"))
	alfa_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="ALFA"))
	aston_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="ASTON"))
	audi_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="AUDI"))
	bmw_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="BMW"))
	fiat_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="FIAT"))
	ford_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="FORD"))
	hyundai_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="Hyundai"))
	honda_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="HONDA"))
	mazda_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="MAZDA"))
	nissan_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="NISSAN"))
	toyota_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="TOYOTA"))
	mitsubishi_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="MITSUBISHI"))
	unknown_trucks_list = list(Vehicle.objects.filter(type="TRUCK", showroom="N", make="Unknown"))
	
	
	variables = RequestContext(request, {
								'mitsubishi_trucks' : mitsubishi_trucks_list,
								'blank_trucks' : blank_trucks_list,
								'daf_trucks' : daf_trucks_list, 
								'erf_trucks' : erf_trucks_list, 
								'iveco_trucks' : iveco_trucks_list, 
								'merc_trucks' : merc_trucks_list, 
								'merc_trucks' : merc_trucks_list, 
								'scania_trucks' : scania_trucks_list, 
								'volvo_trucks' : volvo_trucks_list, 
								'nissan_trucks' : nissan_trucks_list, 
								'golf_trucks' : golf_trucks_list, 
								'renault_trucks' : renault_trucks_list, 
								'foden_trucks' : foden_trucks_list,
								
								'acura_trucks' : acura_trucks_list,
								'alfa_trucks' : alfa_trucks_list,
								'aston_trucks' : aston_trucks_list,
								'audi_trucks' : audi_trucks_list,
								'bmw_trucks' : bmw_trucks_list,
								'fiat_trucks' : fiat_trucks_list,
								'ford_trucks' : ford_trucks_list,
								'hyundai_trucks' : hyundai_trucks_list,
								'honda_trucks' : honda_trucks_list,
								'mazda_trucks' : mazda_trucks_list,
								'toyota_trucks' : toyota_trucks_list,
								'unknown_trucks' : unknown_trucks_list
							}
						)
	return render_to_response('stock_trucks.html', variables)

# ---------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------#

def stock_pickups(request):
	blank_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make=""))
	daf_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="Leyland DAF"))
	erf_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="ERF"))
	iveco_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="IVECO"))
	merc_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="MERCEDES-BENZ"))
	volvo_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="VOLVO"))
	foden_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="Foden"))
	scania_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="SCANIA"))
	renault_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="RENAULT"))
	
	acura_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="ACURA"))
	alfa_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="ALFA"))
	aston_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="ASTON"))
	audi_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="AUDI"))
	bmw_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="BMW"))
	fiat_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="FIAT"))
	ford_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="FORD"))
	hyundai_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="Hyundai"))
	honda_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="HONDA"))
	mazda_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="MAZDA"))
	toyota_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="TOYOTA"))
	unknown_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="Unknown"))
	nissan_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="NISSAN"))
	mitsubishi_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="MITSUBISHI"))
	golf_pickups_list = list(Vehicle.objects.filter(type="4 X 4 PICKUP", showroom="N", make="GOLF"))
	
	
	variables = RequestContext(request, {
								'blank_pickups' : blank_pickups_list,
								'mitsubishi_pickups' : mitsubishi_pickups_list,
								'daf_pickups' : daf_pickups_list, 
								'erf_pickups' : erf_pickups_list, 
								'iveco_pickups' : iveco_pickups_list, 
								'merc_pickups' : merc_pickups_list, 
								'merc_pickups' : merc_pickups_list, 
								'scania_pickups' : scania_pickups_list, 
								'volvo_pickups' : volvo_pickups_list, 
								'renault_pickups' : renault_pickups_list, 
								'foden_pickups' : foden_pickups_list,
								'nissan_pickups' : nissan_pickups_list,
								'golf_pickups' : golf_pickups_list,
								
								'acura_pickups' : acura_pickups_list,
								'alfa_pickups' : alfa_pickups_list,
								'aston_pickups' : aston_pickups_list,
								'audi_pickups' : audi_pickups_list,
								'bmw_pickups' : bmw_pickups_list,
								'fiat_pickups' : fiat_pickups_list,
								'ford_pickups' : ford_pickups_list,
								'hyundai_pickups' : hyundai_pickups_list,
								'honda_pickups' : honda_pickups_list,
								'mazda_pickups' : mazda_pickups_list,
								'toyota_pickups' : toyota_pickups_list,
								'unknown_pickups' : unknown_pickups_list
							}
						)
	return render_to_response('stock_pickups.html', variables)

# ---------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------#

def stock_cars(request):
	blank_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make=""))
	daf_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="Leyland DAF"))
	erf_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="ERF"))
	iveco_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="IVECO"))
	merc_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="MERCEDES-BENZ"))
	volvo_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="VOLVO"))
	foden_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="Foden"))
	scania_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="SCANIA"))
	renault_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="RENAULT"))
	nissan_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="NISSAN"))
	golf_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="GOLF"))
	
	acura_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="ACURA"))
	alfa_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="ALFA"))
	aston_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="ASTON"))
	audi_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="AUDI"))
	bmw_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="BMW"))
	fiat_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="FIAT"))
	ford_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="FORD"))
	hyundai_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="Hyundai"))
	honda_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="HONDA"))
	mazda_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="MAZDA"))
	toyota_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="TOYOTA"))
	unknown_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="Unknown"))
	mitsubishi_cars_list = list(Vehicle.objects.filter(type="CAR", showroom="N", make="MITSUBISHI"))
	
	
	variables = RequestContext(request, {
								'blank_cars' : blank_cars_list,
								'mitsubishi_cars' : mitsubishi_cars_list, 
								'daf_cars' : daf_cars_list, 
								'erf_cars' : erf_cars_list, 
								'iveco_cars' : iveco_cars_list, 
								'merc_cars' : merc_cars_list, 
								'merc_cars' : merc_cars_list, 
								'scania_cars' : scania_cars_list, 
								'volvo_cars' : volvo_cars_list, 
								'renault_cars' : renault_cars_list, 
								'foden_cars' : foden_cars_list,
								'nissan_cars' : nissan_cars_list,
								'golf_cars' : golf_cars_list,
								
								'acura_cars' : acura_cars_list,
								'alfa_cars' : alfa_cars_list,
								'aston_cars' : aston_cars_list,
								'audi_cars' : audi_cars_list,
								'bmw_cars' : bmw_cars_list,
								'fiat_cars' : fiat_cars_list,
								'ford_cars' : ford_cars_list,
								'hyundai_cars' : hyundai_cars_list,
								'honda_cars' : honda_cars_list,
								'mazda_cars' : mazda_cars_list,
								'toyota_cars' : toyota_cars_list,
								'unknown_cars' : unknown_cars_list
							}
						)
	return render_to_response('stock_cars.html', variables)

# ---------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------#
def stock_showroomAll(request):
    veh_list = list(Vehicle.objects.filter(showroom="Y"))
    #if not props_list:
        #raise Http404
    return render_to_response('stock_showroomAll.html', {'vehs': veh_list})

def stock_showroom_search(request):
	
	if request.method == "POST":
		#veh_make = request.POST['make']
		veh_type = request.POST['type']
		
	if veh_type == "0":
		veh_list = list(Vehicle.objects.filter(showroom="Y"))
	else:
		veh_list = list(Vehicle.objects.filter(showroom="Y", type=veh_type))

	return render_to_response('stock_showroomAll.html', {"vehs": veh_list}, context_instance=RequestContext(request))

def stock_showroom(request):
	blank_showroom_list = list(Vehicle.objects.filter(showroom="N", make=""))
	daf_showroom_list = list(Vehicle.objects.filter(showroom="N", make="Leyland DAF"))
	erf_showroom_list = list(Vehicle.objects.filter(showroom="N", make="ERF"))
	iveco_showroom_list = list(Vehicle.objects.filter(showroom="N", make="IVECO"))
	merc_showroom_list = list(Vehicle.objects.filter(showroom="N", make="MERCEDES-BENZ"))
	volvo_showroom_list = list(Vehicle.objects.filter(showroom="N", make="VOLVO"))
	foden_showroom_list = list(Vehicle.objects.filter(showroom="N", make="Foden"))
	scania_showroom_list = list(Vehicle.objects.filter(showroom="N", make="SCANIA"))
	renault_showroom_list = list(Vehicle.objects.filter(showroom="N", make="RENAULT"))
	nissan_showroom_list = list(Vehicle.objects.filter(showroom="N", make="NISSAN"))
	golf_showroom_list = list(Vehicle.objects.filter(showroom="N", make="GOLF"))
	
	acura_showroom_list = list(Vehicle.objects.filter(showroom="N", make="ACURA"))
	alfa_showroom_list = list(Vehicle.objects.filter(showroom="N", make="ALFA"))
	aston_showroom_list = list(Vehicle.objects.filter(showroom="N", make="ASTON"))
	audi_showroom_list = list(Vehicle.objects.filter(showroom="N", make="AUDI"))
	bmw_showroom_list = list(Vehicle.objects.filter(showroom="N", make="BMW"))
	fiat_showroom_list = list(Vehicle.objects.filter(showroom="N", make="FIAT"))
	ford_showroom_list = list(Vehicle.objects.filter(showroom="N", make="FORD"))
	hyundai_showroom_list = list(Vehicle.objects.filter(showroom="N", make="Hyundai"))
	honda_showroom_list = list(Vehicle.objects.filter(showroom="N", make="HONDA"))
	mazda_showroom_list = list(Vehicle.objects.filter(showroom="N", make="MAZDA"))
	toyota_showroom_list = list(Vehicle.objects.filter(showroom="N", make="TOYOTA"))
	unknown_showroom_list = list(Vehicle.objects.filter(showroom="N", make="Unknown"))
	mitsubishi_showroom_list = list(Vehicle.objects.filter(showroom="N", make="MITSUBISHI"))
	
	
	variables = RequestContext(request, {
								'blank_showroom' : blank_showroom_list,
								'mitsubishi_showroom' : mitsubishi_showroom_list, 
								'daf_showroom' : daf_showroom_list, 
								'erf_showroom' : erf_showroom_list, 
								'iveco_showroom' : iveco_showroom_list, 
								'merc_showroom' : merc_showroom_list, 
								'merc_showroom' : merc_showroom_list, 
								'scania_showroom' : scania_showroom_list, 
								'volvo_showroom' : volvo_showroom_list, 
								'renault_showroom' : renault_showroom_list, 
								'foden_showroom' : foden_showroom_list,
								'nissan_showroom' : nissan_showroom_list,
								'golf_showroom' : golf_showroom_list,
								
								'acura_showroom' : acura_showroom_list,
								'alfa_showroom' : alfa_showroom_list,
								'aston_showroom' : aston_showroom_list,
								'audi_showroom' : audi_showroom_list,
								'bmw_showroom' : bmw_showroom_list,
								'fiat_showroom' : fiat_showroom_list,
								'ford_showroom' : ford_showroom_list,
								'hyundai_showroom' : hyundai_showroom_list,
								'honda_showroom' : honda_showroom_list,
								'mazda_showroom' : mazda_showroom_list,
								'toyota_showroom' : toyota_showroom_list,
								'unknown_showroom' : unknown_showroom_list
							}
						)
	return render_to_response('stock_showroom.html', variables)

# ---------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------#

#"""'pics_list':pics_list, 'first_pic': first_pic"""
def detail(request, vehicle_id):
    try:
        v = Vehicle.objects.get(pk=vehicle_id)
        pics_list = v.picture_set.all()
	email_list = list(ContactDetail.objects.filter(location='United Kingdom', email='henry@techmiyacommercials.co.uk'))
    except Vehicle.DoesNotExist:
        raise Http404
    return render_to_response('vehicle_info.html', {'v' : v, 'pics' : pics_list, 'email_list' : email_list})
	
# ---------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------#

def contacts(request):
	uk_contacts_list = list(ContactDetail.objects.filter(location="United Kingdom"))
	zambia_contacts_list = list(ContactDetail.objects.filter(location = "Zambia"))
	namibia_contacts_list = list(ContactDetail.objects.filter(location = "Namibia"))
	congo_contacts_list = list(ContactDetail.objects.filter(location = "Congo"))
	burundi_contacts_list = list(ContactDetail.objects.filter(location = "Burundi"))
	botswana_contacts_list = list(ContactDetail.objects.filter(location = "Botswana"))
	tanzania_contacts_list = list(ContactDetail.objects.filter(location = "Tanzania"))
	malawi_contacts_list = list(ContactDetail.objects.filter(location = "Malawi"))
	
	variables = RequestContext(request, {
								'uk' : uk_contacts_list, 
								'zambia' : zambia_contacts_list, 
								'namibia' : namibia_contacts_list,
								'congo' : congo_contacts_list,
								'burundi' : burundi_contacts_list,
								'botswana' : botswana_contacts_list,
								'tanzania' : tanzania_contacts_list,
								'malawi' : malawi_contacts_list
									}
								)
	
	return render_to_response('contacts.html', variables)

	
def stock_trailers(request):
	blank_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make=""))
	daf_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="Leyland DAF"))
	erf_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="ERF"))
	iveco_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="IVECO"))
	merc_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="MERCEDES-BENZ"))
	volvo_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="VOLVO"))
	foden_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="Foden"))
	scania_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="SCANIA"))
	renault_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="RENAULT"))
	
	acura_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="ACURA"))
	alfa_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="ALFA"))
	aston_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="ASTON"))
	audi_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="AUDI"))
	bmw_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="BMW"))
	fiat_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="FIAT"))
	ford_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="FORD"))
	hyundai_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="Hyundai"))
	honda_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="HONDA"))
	mazda_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="MAZDA"))
	toyota_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="TOYOTA"))
	unknown_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="Unknown"))
	nissan_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="NISSAN"))
	golf_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="GOLF"))
	mitsubishi_trailers_list = list(Vehicle.objects.filter(type="TRAILER", showroom="N", make="MITSUBISHI"))
	
	
	variables = RequestContext(request, {
								'blank_trailers' : blank_trailers_list,
								'mitsubishi_trailers' : mitsubishi_trailers_list,
								'daf_trailers' : daf_trailers_list, 
								'erf_trailers' : erf_trailers_list, 
								'iveco_trailers' : iveco_trailers_list, 
								'merc_trailers' : merc_trailers_list, 
								'merc_trailers' : merc_trailers_list, 
								'scania_trailers' : scania_trailers_list, 
								'volvo_trailers' : volvo_trailers_list, 
								'renault_trailers' : renault_trailers_list, 
								'foden_trailers' : foden_trailers_list,
								'nissan_trailers' : nissan_trailers_list,
								'golf_trailers' : golf_trailers_list,
								
								'acura_trailers' : acura_trailers_list,
								'alfa_trailers' : alfa_trailers_list,
								'aston_trailers' : aston_trailers_list,
								'audi_trailers' : audi_trailers_list,
								'bmw_trailers' : bmw_trailers_list,
								'fiat_trailers' : fiat_trailers_list,
								'ford_trailers' : ford_trailers_list,
								'hyundai_trailers' : hyundai_trailers_list,
								'honda_trailers' : honda_trailers_list,
								'mazda_trailers' : mazda_trailers_list,
								'toyota_trailers' : toyota_trailers_list,
								'unknown_trailers' : unknown_trailers_list
							}
						)
	return render_to_response('stock_trailers.html', variables)
	
def stock_machinery(request):
	blank_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make=""))
	daf_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="Leyland DAF"))
	erf_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="ERF"))
	iveco_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="IVECO"))
	merc_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="MERCEDES-BENZ"))
	volvo_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="VOLVO"))
	foden_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="Foden"))
	scania_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="SCANIA"))
	renault_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="RENAULT"))
	
	acura_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="ACURA"))
	alfa_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="ALFA"))
	aston_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="ASTON"))
	audi_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="AUDI"))
	bmw_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="BMW"))
	fiat_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="FIAT"))
	ford_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="FORD"))
	hyundai_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="Hyundai"))
	honda_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="HONDA"))
	mazda_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="MAZDA"))
	toyota_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="TOYOTA"))
	unknown_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="Unknown"))
	nissan_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="NISSAN"))
	golf_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="GOLF"))
	mitsubishi_machinery_list = list(Vehicle.objects.filter(type="MACHINERY & EQUIPS", showroom="N", make="MITSUBISHI"))
	
	
	variables = RequestContext(request, {
								'blank_machinery' : blank_machinery_list,
								'daf_machinery' : daf_machinery_list, 
								'erf_machinery' : erf_machinery_list, 
								'iveco_machinery' : iveco_machinery_list, 
								'merc_machinery' : merc_machinery_list, 
								'merc_machinery' : merc_machinery_list, 
								'scania_machinery' : scania_machinery_list, 
								'volvo_machinery' : volvo_machinery_list, 
								'renault_machinery' : renault_machinery_list, 
								'foden_machinery' : foden_machinery_list,
								'nissan_machinery' : nissan_machinery_list,
								'golf_machinery' : golf_machinery_list,
								'mitsubishi_machinery' : mitsubishi_machinery_list,								
								'acura_machinery' : acura_machinery_list,
								'alfa_machinery' : alfa_machinery_list,
								'aston_machinery' : aston_machinery_list,
								'audi_machinery' : audi_machinery_list,
								'bmw_machinery' : bmw_machinery_list,
								'fiat_machinery' : fiat_machinery_list,
								'ford_machinery' : ford_machinery_list,
								'hyundai_machinery' : hyundai_machinery_list,
								'honda_machinery' : honda_machinery_list,
								'mazda_machinery' : mazda_machinery_list,
								'toyota_machinery' : toyota_machinery_list,
								'unknown_machinery' : unknown_machinery_list
							}
						)
	return render_to_response('stock_machinery.html', variables)
