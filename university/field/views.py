from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from field.forms import *

# Create your views here.
def home(request):
	return render(request,'field/home.html')

def base(request):
	return render(request,'field/base.html')

def profile(request):
	y=Profile.objects.all()
	context = {
		'y':y
	}
	return render(request,'field/profile.html',context)

def apply(request):
	form = FieldApplicationForm()
	if request.method=='POST':
		form=FieldApplicationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'data created successfully')
			return redirect('home')
	context = {
		'form': form
	}
	return render(request,'field/apply.html',context)

def selected(request):
	x=FieldApplication.objects.all()
	context={
		'x':x
	}
	return render(request,'field/selected.html',context)

def team(request):
	return render(request,'field/team.html')

def applied(request):
	x=FieldApplication.objects.all()
	if request.method=='POST':
		id_list = request.POST.getlist('boxes')

		#uncheck all events
		x.update(approved=False)

		#update list
		for i in id_list:
			FieldApplication.objects.filter(pk=int(i)).update(approved=True)
		return redirect('applied')

	context={
	 	'x':x
	}
	return render(request,'field/applied.html',context)

def signin(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password1 = request.POST.get('password1')
		user = authenticate(username=username,password=password1)

		if user is not None:
			login(request,user)
			
			return render(request,'field/home.html')

		else:
			messages.error(request,'Bad authenticate')
			return redirect('signin')


	return render(request,'field/signin.html')

def signup(request):
	if request.method == 'POST':
		username=request.POST['username']
		firstname=request.POST['firstname']
		lastname=request.POST['lastname']
		email=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']

		myuser=User.objects.create_user(username,email,password1)
		myuser.first_name=firstname
		myuser.last_name=lastname
		myuser.save()
		messages.success(request,'You registered successfully')
		return redirect('signin')
	return render(request,'field/signup.html')

def signout(request):
	logout(request)
	messages.success(request,"you logged out successfully")
	return redirect('home')
	return render(request,'form/signout.html')
