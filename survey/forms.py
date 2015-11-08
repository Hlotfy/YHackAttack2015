from django import forms

class SomeForm(forms.Form):
	YES = 1
	NO = 0
	CHOICES = ((YES,'yes'), (NO,'no'),)
	answer = forms.MultipleChoiceField(choices=CHOICES)




