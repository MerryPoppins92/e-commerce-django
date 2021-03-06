from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

def home_page(request):
	context = {
		"title":"Hello World!",
		"content":"Welcome to the home page"
		
	}
	if request.user.is_authenticated:
		context["premium_content"] = "yeahhh"
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title":"About!",
		"content":"Welcome to the About page"
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title":"Contact!",
		"content":"Welcome to the Contact page",
		"form": contact_form,
	}
	if contact_form.errors:
		print(contact_form.cleaned_data)
		errors = contact_form.errors.as_json()
		if request.is_ajax():
			return HttpResponse(errors, status=400, content_type = 'application/json')

	if contact_form.is_valid():
		print(contact_form.cleaned_data)
		if request.is_ajax():
			return JsonResponse({"message": "Thank You"})

	# if request.method == "POST":
	# 	print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, "contact/view.html", context)
