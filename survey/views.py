
from django.shortcuts import render
from .forms import SomeForm
from django.http import HttpResponseRedirect
from .models import SurveyResponse

# Create your views here.
def home(request):
	return render(request, "home.html", {})

def some_view(request):
	someresponse = []
	if request.method == 'POST':
		form = SomeForm(request.POST)
		if form.is_valid():
			all_answer = form.cleaned_data.get("answer")
			
			for i in all_answer:
				surveyanswer = SurveyResponse(answer = int(i))
				someresponse.append(surveyanswer.answer)
			
			responsenumber = sum(someresponse)

			# different legislators for different responsenumber
			if responsenumber == 1:
				return HttpResponseRedirect('/thanks/')

	else:
		form = SomeForm

	return render(request,'some_template.html', {'form':form, 'someresponse':someresponse})
    
            #surveyanswer.save()

            # redirect to new URL
            # return HttpResponseRedirect('/thanks/')
            # do something with your results



    #someresponse = []
    #for object in SurveyResponse.objects.all():
    #	someresponse.append(object)