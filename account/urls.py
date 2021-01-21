from django.urls import path
from django.contrib.auth import views as auth_views
from account import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),

    # view functionaillty
    path('updateOrder/<str:pk>/', views.updateOrder, name='updateOrder'),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name='deleteOrder'),
    path('createOrder/<str:pk>/', views.createOrder, name='createOrder'),

    # Registration & Login
    path('login/', views.loginPage, name='login'),
    path('register/', views.resgisterPage, name='register'),
    path('logout/', views.logoutuser, name='logout'),

    # User Settings
    path('user/', views.userPage, name='userPage'),
    path('account_settings/', views.account_settings, name='account'),

    # Password Reset
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_success/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset_done.html'),
         name='password_reset_complete'),

    path('createuser/', views.createuser, name='createuser'),

]
