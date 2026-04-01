from django.db import models


class Employee(models.Model):
    emp_id = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    salary = models.FloatField()
    company = models.CharField(max_length=50)
    email_address = models.EmailField()
