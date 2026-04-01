from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.views import View
from .forms import EmployeeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class EmployeeCreate(LoginRequiredMixin, View):
    template_name = 'employee_app/employee_create.html'

    def get(self, request):
        form = EmployeeForm()
        context = {'form': form}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
        context = {'form': form}
        return render(request, self.template_name, context=context)


class EmployeeList(LoginRequiredMixin, View):
    template_name = 'employee_app/employee_list.html'

    def get(self, request):
        employees = Employee.objects.all()
        context = {'employees': employees}
        return render(request, self.template_name, context=context)


class EmployeeUpdate(LoginRequiredMixin, View):
    template_name = 'employee_app/employee_update.html'

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        form = EmployeeForm(instance=employee)
        context = {'form': form}
        return render(request, self.template_name, context=context)

    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
        context = {'form': form}
        return render(request, self.template_name, context=context)


class EmployeeDelete(LoginRequiredMixin, View):
    template_name = 'employee_app/employee_confirm_delete.html'

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        context = {'employee': employee}
        return render(request, self.template_name, context=context)

    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return redirect('employee-list')


class UserRegister(View):
    template_name = 'employee_app/user_create.html'

    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context = {'form': form}
        return render(request, self.template_name, context=context)


def custom_404(request, exception):
    return render(request, 'custom404.html', status=404)
