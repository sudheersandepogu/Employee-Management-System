from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import EmployeeForm
from .models import Employee, Department


def login_view(request):
    if request.user.is_authenticated:
        return redirect("employees:dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("employees:dashboard")
        messages.error(request, "Invalid username or password.")

    return render(request, "employees/login.html")


def logout_view(request):
    logout(request)
    return redirect("employees:login")


@login_required
def dashboard(request):
    active_count = Employee.objects.filter(status="active").count()
    leave_count = Employee.objects.filter(status="on_leave").count()
    total_count = Employee.objects.count()
    dept_count = Department.objects.count()
    
    employees = Employee.objects.order_by("-date_of_joining")[:5]
    
    # Department distribution for chart
    from django.db.models import Count
    dept_stats = Department.objects.annotate(emp_count=Count('employees')).order_by('-emp_count')[:6]
    
    return render(request, "employees/dashboard.html", {
        "active_count": active_count,
        "leave_count": leave_count,
        "total_count": total_count,
        "dept_count": dept_count,
        "employees": employees,
        "dept_stats": dept_stats,
    })


@login_required
def employee_list(request):
    query = request.GET.get("q", "")
    employees = Employee.objects.all()
    if query:
        employees = employees.filter(
            Q(employee_code__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(department__name__icontains=query)
            | Q(designation__name__icontains=query)
        )
    return render(request, "employees/employee_list.html", {
        "employees": employees,
        "query": query,
    })


@login_required
def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Employee record created successfully.")
        return redirect("employees:employee_list")
    return render(request, "employees/employee_form.html", {"form": form, "title": "Add Employee"})


@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        messages.success(request, "Employee record updated successfully.")
        return redirect("employees:employee_list")
    return render(request, "employees/employee_form.html", {"form": form, "title": "Edit Employee"})


@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        messages.success(request, "Employee record deleted successfully.")
        return redirect("employees:employee_list")
    return render(request, "employees/employee_confirm_delete.html", {"employee": employee})
