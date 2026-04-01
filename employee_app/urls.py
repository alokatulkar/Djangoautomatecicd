from django.urls import path
from .views import EmployeeCreate, EmployeeList, EmployeeUpdate, EmployeeDelete, UserRegister
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('employee/', EmployeeCreate.as_view(), name='employee-create'),
    path('employee_list/', EmployeeList.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeUpdate.as_view(), name='employee-update'),
    path('employee_delete/<int:pk>/', EmployeeDelete.as_view(), name='employee-delete'),
    path('register/', UserRegister.as_view(), name='register'),
    path('', LoginView.as_view(template_name='employee_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
