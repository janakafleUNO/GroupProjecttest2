from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from .forms import CustomUserCreationForm

now = timezone.now()
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# HomePage
def home(request):
    return render(request, 'carviewer/home.html',
                  {'carviewer': home})


# CarBrand
@login_required
def carbrand_list(request):
    carbrand = CarBrand.objects.filter()
    return render(request, 'carviewer/carbrand_list.html',
                  {'carbrands': carbrand})


# CarType
@login_required
def cartype_list(request):
    cartype = CarType.objects.filter()
    return render(request, 'carviewer/cartype_list.html',
                  {'cartypes': cartype})


# CarModel
@login_required
def carmodel_list(request):
    carmodel = CarModel.objects.filter()
    return render(request, 'carviewer/carmodel_list.html',
                  {'carmodels': carmodel})


# CarReview
@login_required
def carreview_list(request):
    carreview = CarReview.objects.filter()
    return render(request, 'carviewer/carreview_list.html',
                  {'carreviews': carreview})


@login_required
def carreview_new(request):
    if request.method == "POST":
        form = CarReviewForm(request.POST)
        if form.is_valid():
            carreview = form.save(commit=False)
            carreview.created_date = timezone.now()
            carreview.save()
            carreview = CarReview.objects.filter()
            return render(request, 'carviewer/carreview_list.html',
                          {'carreviews': carreview})
    else:
        form = CarReviewForm()

    return render(request, 'carviewer/carreview_new.html', {'form': form})


@login_required
def carreview_edit(request, pk):
    carreview = get_object_or_404(CarReview, pk=pk)
    if request.method == "POST":
        form = CarReviewForm(request.POST, instance=carreview)
        if form.is_valid():
            carreview = form.save()
            carreview.updated_date = timezone.now()
            carreview.save()
            carreview = CarReview.objects.filter()
            return render(request, 'carviewer/carreview_list.html', {'carreviews': carreview})
    else:
        form = CarReviewForm(instance=carreview)
    return render(request, 'carviewer/carreview_edit.html', {'form': form})


@login_required
def carreview_delete(request, pk):
    carreview = get_object_or_404(CarReview, pk=pk)
    carreview.delete()
    return redirect('carviewer:carreview_list')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
