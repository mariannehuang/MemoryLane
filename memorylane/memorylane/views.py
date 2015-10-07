from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Memory
#def signup(request):
#	return render(request, 'signup.html', {})

def profiletest(request, user_id):
	u = User.objects.get(pk=user_id)
	output = ("<h1>You're looking at user %s.</h1>" % user_id)
	
	output = output + "<br>" + u.first_name + " " + u.last_name


	return HttpResponse(output)

def userlist(request):
	lastest_user_list = User.objects.order_by('pk')[:5]
	output = ', '.join([u.first_name for u in lastest_user_list])
	return HttpResponse(output)