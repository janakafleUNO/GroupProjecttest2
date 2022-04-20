from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CarBrand, CarType, CarModel, CarReview


class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ('car_brand', 'car_year', 'car_image')


class CarTypeForm(forms.ModelForm):
    class Meta:
        model = CarType
        fields = ('car_brand', 'car_image', 'car_bodytype', 'car_fueltype', 'car_transmission', 'description', 'available')


class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = (
            'car_brand', 'car_year', 'model_name', 'car_image',  'car_bodytype', 'car_fueltype', 'car_transmission', 'car_price',
            'car_mileage')


class CarReviewForm(forms.ModelForm):
    class Meta:
        model = CarReview
        fields = ('car_brand', 'car_year', 'model_name', 'car_image', 'car_bodytype', 'car_expert_review', 'car_user_review',
                  'car_overall_review')


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def __init__(self, *args, **kwargs):
    super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
        field.widget.attrs.update({'class': 'form-control'})
