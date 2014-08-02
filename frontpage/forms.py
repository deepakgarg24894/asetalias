from django import forms

class register_form(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()
	subject=forms.CharField()
	message=forms.CharField()


