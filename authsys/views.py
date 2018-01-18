from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth


def login(request):

	login_errors = ''
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect("/")
		else:
			login_errors = 'User not exist'
			#context = {'login_error': login_error}
			return render(request, 'auth/login.html', {'context': login_errors})
	else:
		return render(request, 'auth/login.html', {'context': login_errors})


def logout(request):
	auth.logout(request)
	return redirect('/')