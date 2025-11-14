from django.contrib import admin
from .models import Employee, Department, Role

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'dept',
        'role',
        'salary',
        'bonus',
        'total_compensation',
        'hire_date',
    )
    search_fields = ('firstname', 'lastname')
    ordering = ('-hire_date','salary')
    date_hierarchy = 'hire_date'
    list_editable = ('salary', 'bonus')   # both now in list_display
    readonly_fields = ('hire_date',)
    
    def full_name(self, obj):
        return f"{obj.firstname} {obj.lastname}"
    full_name.short_description = "Full Name"

    def total_compensation(self, obj):
        return obj.salary + obj.bonus
    total_compensation.short_description = "Salary + Bonus"


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'employee_count')
    list_filter = ('name',)
    search_fields = ('name',)

    def employee_count(self, obj):
        return obj.emp_dept.count()   # emp_dept is your related_name
    employee_count.short_description = 'No. of Employees'

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role','employee_count')
    search_fields = ('role',)

    def employee_count (self, obj):
        return obj.emp_role.count()
    employee_count.short_description = "NO. OF EMPLOYEE"