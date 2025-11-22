from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('enrollee/', views.enrollee_view, name='enrollee'),
    path('enrollee/view/', views.view_information, name='view_info'),
    path('logout/', views.logged_out_view, name='logged_out'),
    path('logout/<str:name>/', views.logged_out_with_name, name='logged_out_with_name'),
]
 
