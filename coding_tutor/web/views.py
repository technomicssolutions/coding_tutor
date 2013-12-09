# Create your views here.
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from web.models import *

class Home(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home.html',context)

class SignUp(View):

    def get(self, request, *args, **kwargs):
        template = 'registration/register.html'
        return render(request, template, {})

    def post(self, request, *args, **kwargs):

    	print "a"*10,request.POST

    	first_name =  request.POST['first_name']
    	last_name = request.POST['last_name']
    	email = request.POST['email']

    	course = request.POST['course']
    	description = course

    	month = request.POST['month']
    	verification_code = request.POST['verification_code']
    	year = request.POST['year']
    	card_number = request.POST['card_number']
    	user = User.objects.create(first_name=first_name, last_name=last_name,
            email=email, username=email)
    	user.set_password(card_number)
    	user.save()
    	course = Course.objects.create(name=course,description=description)
    	userprofile = UserProfile.objects.create(user=user,course=course,verification_code=verification_code,card_number=card_number)
    	userprofile.save()
    	return HttpResponse({'succes': True})

