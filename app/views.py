from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import Data
from app.forms import FormData
# Create your views here.

def index(request):
	error = False
	success = False
	if request.method == 'POST':
		form = FormData(request.POST)
		if form.is_valid():
			q = Data(url=form.cleaned_data['url'], slug=form.cleaned_data['slug'])
			q.save()
			success = True
		else:
			error = True
	else:
		form = FormData()

	return render(request, 'app/index.html', {'form':form, 'error':error, 'success':success})

def goto(request, slug):
    data = Data.objects.filter(slug=slug)
    if data:
        return redirect(data[0].url)
    return render(request, 'app/error.html')
