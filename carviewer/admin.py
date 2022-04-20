from django.contrib import admin
from .models import CarType, CarBrand, CarModel, CarReview


class CarBrandList(admin.ModelAdmin):
    list_display = ('car_brand', 'car_year', 'car_image')
    list_filter = ('car_brand', 'car_year', 'car_image')
    ordering = ['car_brand']


class CarTypeList(admin.ModelAdmin):
    list_display = ('car_brand', 'car_image', 'car_bodytype', 'car_fueltype', 'car_transmission')
    list_filter = ('car_brand', 'car_image', 'car_bodytype', 'car_fueltype')
    search_fields = ('car_brand', 'car_image', 'car_bodytype', 'car_fueltype', 'car_transmission')
    ordering = ['car_brand']


class CarModelList(admin.ModelAdmin):
    list_display = (
        'car_brand', 'car_year', 'model_name', 'car_image', 'car_bodytype', 'car_fueltype', 'car_transmission',
        'car_price',
        'car_mileage')
    list_filter = (
        'car_brand', 'car_year', 'model_name', 'car_image', 'car_bodytype', 'car_fueltype', 'car_transmission',
        'car_price',)
    search_fields = ('car_brand', 'car_year', 'model_name', 'car_image')
    ordering = ['car_brand']


class CarReviewList(admin.ModelAdmin):
    list_display = (
        'car_brand', 'car_year', 'model_name', 'car_image', 'car_bodytype', 'car_expert_review', 'car_user_review',
        'car_overall_review')

    list_filter = (
        'car_brand', 'car_year', 'model_name', 'car_image', 'car_bodytype', 'car_expert_review', 'car_user_review',
        'car_overall_review')
    search_fields = ('car_brand', 'car_year', 'model_name', 'car_image', 'car_expert_review')
    ordering = ['car_brand']


admin.site.register(CarBrand, CarBrandList)
admin.site.register(CarType, CarTypeList)
admin.site.register(CarModel, CarModelList)
admin.site.register(CarReview, CarReviewList)
