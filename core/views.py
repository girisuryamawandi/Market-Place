from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from item.models import Category, Item
from .forms import LoginForm, SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })



def loginView(request):
	context = {
		'page_title':'LOGIN',
        'forms' : LoginForm
	}
	user = None
	if request.method == "POST":
		
		username_login = request.POST['username']
		password_login = request.POST['password']
		
		user = authenticate(request, username=username_login, password=password_login)

		if user is not None:
			login(request, user)
			return redirect('core:index')
		else:
			return redirect('core:login')
		
	return render(request, 'core/login.html', context)

def contact(request):
    return render(request,'core/contact.html')


def logoutView(request):
	context = {
		'page_title':'logout'
	}

	if request.method == "POST":
		if request.POST["logout"] == "Submit":
			logout(request)

		return redirect('core:index')	


	return render(request, 'core/logout.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })