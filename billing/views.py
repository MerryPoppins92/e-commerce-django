from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url


import stripe
stripe.api_key = "sk_test_51HeFtLD0vNzmZbktiSjWa72MusSqTp5YxGHu1u2Le8UhGUBSoqPtyD5DvqS6iIMoRDrgNu6L7jXKE9yFs0TmJdUN00TAQVRuR4"
STRIPE_PUB_KEY = 'pk_test_51HeFtLD0vNzmZbktnCLQCdWhQI5fhePzJMADtUmvOtlVWXKIXvrLHxoTtPvk7WvKahppAh5YmMAFXlHE2IHt58aR00XCuptAC1'

from .models import BillingProfile, Card

def payment_method_view(request):
	# if request.user.is_authenticated:
	# 	billing_profile = request.user.billingprofile
	# 	my_customer_id = billing_profile.customer_id

	billing_profile, billing_guest_profile_created = BillingProfile.objects.new_or_get(request)
	if not billing_profile:
		return redirect("/cart")
	next_url = None
	next_ = request.GET.get('next')
	if is_safe_url(next_, request.get_host()):
		next_url = next_
	return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY, "next_url": next_url})

def payment_method_create_view(request):

	if request.method == "POST" and request.is_ajax():
		billing_profile, billing_guest_profile_created = BillingProfile.objects.new_or_get(request)
		print(billing_profile)
		if not billing_profile:
			return HttpResponse({"message": "Cannot find this user"}, status_code = 401)
		print(request.POST)
		token = request.POST.get("token")
		print(token)
		if token is not None:
			customer = stripe.Customer.retrieve(billing_profile.customer_id)
			card_response = customer.create(token)
			print(card_response)
			# card_response.email = billing_profile.email
			# card_response.name = billing_profile.email
			new_card_obj = Card.objects.add_new(billing_profile, card_response)
			print(new_card_obj)
		return JsonResponse({"message":"Success ! Your card was added!"})
	return HttpResponse("error", status_code = 401)


	# if request.method == "POST" and request.is_ajax():
	# 	billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
	# 	if not billing_profile:
 #        	return HttpResponse({"message": "Cannot find this user"}, status_code=401)
 #        token = request.POST.get("token")
 #        if token is not None:
 #            new_card_obj = Card.objects.add_new(billing_profile, token)
 #        return JsonResponse({"message": "Success! Your card was added."})
 #    return HttpResponse("error", status_code=401)

