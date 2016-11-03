import json
from deneme.models import Deneme ,Konu ,Review
from django.shortcuts import render , redirect,get_object_or_404
from deneme.forms import RegistrationForm,ReviewCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
def detail(request, id):
	return render(
        request,
        'konu.html',
        {
            'Konu': get_object_or_404(Konu, id=id),
        }
    )


@login_required(login_url='login')
def like_place(request, konu_id):
	begen = get_object_or_404(Konu, id=konu_id)

	if request.method == "POST":

		if request.user in begen.likes.all():
			begen.likes.remove(request.user)
			action = 'unlike'
		else:
			begen.likes.add(request.user)
			action = 'like'

		if request.is_ajax():
			return HttpResponse(
				json.dumps({
					'count': begen.likes.count(),
					'action': action
				})
			)

	else:
		return HttpResponse('beğenilemedi',status=403)

	return redirect(Konu.get_absolute_url())

def index(request):

    return render(request,"index.html",{"Deneme":Deneme.objects.all(),
										"Konu":Konu.objects.all(),})

@login_required(login_url='login')
def new_review(request, konu_id):
    konu = get_object_or_404(Konu, id=konu_id)
    form = ReviewCreationForm()

    if request.method == "POST":
        form = ReviewCreationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.konu = konu
            form.save()
            return redirect(konu.get_absolute_url())

    return render(
        request,
        'new_review.html',
        {
            'konu': konu,
            'form': form,
        }
    )

@login_required(login_url='login')
def profile(request,id):
	return render(
		request,
		'profile.html',
		{
			'user': get_object_or_404(User, id=id),
			'review': get_object_or_404(Review, id=id),
		}
	)