from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]


class Designation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]


class Employee(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("on_leave", "On Leave"),
        ("inactive", "Inactive"),
    ]

    employee_code = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="employees")
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, blank=True, related_name="employees")
    date_of_joining = models.DateField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="active")
    location = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    avatar_color = models.CharField(max_length=7, default="#0b6ef6", help_text="Hex color for avatar background")

    class Meta:
        ordering = ["employee_code"]
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.employee_code} — {self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def avatar_initials(self):
        return f"{self.first_name[0]}{self.last_name[0]}".upper()
