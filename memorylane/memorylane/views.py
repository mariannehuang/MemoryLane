from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import User, Memory

def profiletest(request, user_id):
	u = User.objects.get(pk=user_id)
	output = ("<h1>You're looking at user %s.</h1>" % user_id)
	
	output = output + "<br>" + u.first_name + " " + u.last_name


	return HttpResponse(output)

def userlist(request):
	lastest_user_list = User.objects.order_by('pk')[:5]
	output = ', '.join([u.first_name for u in lastest_user_list])
	return HttpResponse(output)

def signup(request):
	return render(request, 'signup.html', {})

def settings(request):
	return render(request, 'settings.html', {})

def post(request):
	memory = get_object_or_404(Memory, pk=1)
	author = get_object_or_404(User, pk=memory.author)
	return render(request, 'post.html', {'memory': memory, 'author': author})

def passwordreset(request):
	return render(request, 'password-reset.html', {})

def login(request):
	return render(request, 'login.html', {})

def friends(request):
	return render(request, 'friends.html', {})