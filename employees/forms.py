from django import forms
from .models import Employee, Department, Designation


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "employee_code",
            "first_name",
            "last_name",
            "email",
            "phone",
            "department",
            "designation",
            "date_of_joining",
            "status",
            "location",
            "notes",
            "avatar_color",
        ]
        widgets = {
            "date_of_joining": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "notes": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "avatar_color": forms.TextInput(attrs={"type": "color", "class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")
