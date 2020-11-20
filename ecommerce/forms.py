from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	fullname = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class": "form-control", 
				"placeholder":"Your Full Name", 
				"id":"form_full_name"
					}
				)
		)

	email = forms.EmailField(
		widget = forms.EmailInput(
			attrs = {
				"class": "form-control", 
				"placeholder":"Your Email" 
					}
				)
		)

	content = forms.CharField(
		widget = forms.Textarea(
			attrs = {
				'class':'form-control', 
				'placeholder':'Your Message'
					}
				)
		)

	# def clean_email(self):
	# 	email = self.cleaned_data.get("email")
	# 	if not "gmail.com" in email:
	# 		raise forms.ValidationError("Email has to be gmail.com")
	# 	return email

	# def clean_content(self):
	# 	raise forms.ValidationError("Content is Wrong")
