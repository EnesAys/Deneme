from deneme.models import Deneme
from django.shortcuts import render , redirect
from deneme.forms import RegistrationForm
from django.contrib import messages

def register(request):
	form = RegistrationForm()

	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			form.save()

			messages.info(
				request,
				'Kayıt başarılı. Şimdi login olabilirsiniz.'
			)

			return redirect('login')

	return render(request, 'register-form.html', {
		'form': form,
	})
# Create your views here.
def index(request):

    return render(request,"index.html",{"Deneme":Deneme.objects.all(),})
