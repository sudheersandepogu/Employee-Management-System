from django.contrib import admin
from .models import Department, Designation, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "get_employee_count")
    search_fields = ("name",)
    
    def get_employee_count(self, obj):
        return obj.employees.count()
    get_employee_count.short_description = "Employees"


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ("name", "department")
    list_filter = ("department",)
    search_fields = ("name",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_code",
        "first_name",
        "last_name",
        "department",
        "designation",
        "status",
    )
    list_filter = ("department", "designation", "status")
    search_fields = ("employee_code", "first_name", "last_name", "email")
    fieldsets = (
        ("Basic Info", {"fields": ("employee_code", "first_name", "last_name", "email", "phone")}),
        ("Position", {"fields": ("department", "designation", "date_of_joining")}),
        ("Status", {"fields": ("status", "location")}),
        ("Notes", {"fields": ("notes", "avatar_color")}),
    )
