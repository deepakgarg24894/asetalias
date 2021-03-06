from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from frontpage.forms import register_form
from frontpage.models import messages
from django.contrib import messages as mesg
import pdb


def register(request):
	if request.method=='POST':
		form=register_form(request.POST)
		
		if form.is_valid():
				details=messages(name=form.cleaned_data['name'], email=form.cleaned_data['email'], subject=form.cleaned_data['subject'], message=form.cleaned_data['message'])
				details.save()
				mesg.success(request, "Thanks. We have recieved your message, We will be in touch")
				return render_to_response('index.html',context_instance=RequestContext(request))
		else:
			return render_to_response('index.html',context_instance=RequestContext(request))
	else:
		return render_to_response('index.html',context_instance=RequestContext(request))
