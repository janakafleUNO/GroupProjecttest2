from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'carviewer'

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),

    path('signup/', views.signup, name='signup'),

    path('carbrand_list', views.carbrand_list, name='carbrand_list'),

    path('cartype_list', views.cartype_list, name='cartype_list'),

    path('carmodel_list', views.carmodel_list, name='carmodel_list'),

    path('carreview_list', views.carreview_list, name='carreview_list'),
    path('carreview/create/', views.carreview_new, name='carreview_new'),
    path('carreview/<int:pk>/edit/', views.carreview_edit, name='carreview_edit'),
    path('carreview/<int:pk>/delete/', views.carreview_delete, name='carreview_delete'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

]
