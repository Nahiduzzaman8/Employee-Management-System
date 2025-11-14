from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Role(models.Model):
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.role


class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dept = models.ForeignKey(Department, related_name='emp_dept',on_delete=models.CASCADE)
    role = models.ForeignKey(Role, related_name = 'emp_role',on_delete=models.CASCADE)    
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname