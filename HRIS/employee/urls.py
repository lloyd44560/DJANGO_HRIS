from django.urls import path
from django.conf import settings
from . import views 
from django.contrib.auth.views import LoginView, LogoutView
from .views import pagelogout, manage_employee, add_employee
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', pagelogout, name='logout'),
    path('employees/', manage_employee, name='employee'),
    path('add_employee/', add_employee, name='add_employee'),
    path('edit_employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('update_employee/', views.update_employee, name='update_employee'),
    path('retrieve_employee_info/', views.retrieve_employee_info, name='retrieve_employee_info'),
    ]

