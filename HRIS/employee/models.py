from django.db import models
from django_countries.fields import CountryField


class Employee(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    RELIGION_CHOICES = [
        ('RC', 'Roman Catholic'),
        ('BC', 'Bornagain Christian'),
        ('M',  'Muslim'),
    ]
    CIVIL_STATUS = [
        ('S', 'Single'),
        ('M', 'Married'),
    ]
    EMPLOYEE_STATUS = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]

    employee_id = models.CharField(max_length=50, primary_key = True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES, null = True)
    date_of_birth = models.DateField(null = True)
    place_of_birth = models.CharField(max_length=50,null = True)
    age = models.IntegerField( null = True)
    contact_number = models.IntegerField( null = True)
    religion = models.CharField(max_length=2,choices=RELIGION_CHOICES, null = True)
    civil_status = models.CharField(max_length=2,choices=CIVIL_STATUS, null = True)
    barangay = models.CharField(max_length=50,null = True)
    city = models.CharField(max_length=50,null = True)
    house_number = models.CharField(max_length=50,null = True)
    country = CountryField(null = True, blank=True)
    zip = models.CharField(max_length=50,null = True)
    tin = models.CharField(max_length=50,null = True)
    employee_status = models.CharField(max_length=2,choices=EMPLOYEE_STATUS, null = True)
    country_field = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True) 
    image = models.ImageField(upload_to='employee_images/', null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Bank Information
class BankInformation(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('S', 'Savings'),
        ('C', 'Current'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='bank_information')
    bank_holder_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.bank_holder_name} - {self.bank_name}"

# Departments
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Holiday(models.Model):
    holiday_name = models.CharField(max_length=100)
    holiday_desc = models.TextField()

    def __str__(self):
        return self.holiday_name

class Leaves(models.Model):
    leave_type = models.CharField(max_length=100)
    num_of_days = models.PositiveIntegerField()
    request_type = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.leave_type

        
class Notice(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    attachment = models.FileField(upload_to='notice_attachments/', null=True, blank=True)
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Document(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_url = models.FileField(upload_to='documents/',  null=True)

    def __str__(self):
        return f"{self.file_name} - {self.employee.first_name} {self.employee.last_name}"

class Settings(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    contact_number = models.CharField(max_length=20)
    system_email = models.EmailField()
    company_address = models.TextField()
    logo = models.ImageField(upload_to='company_logo/', null=True, blank=True)

    def __str__(self):
        return self.title
        
# Employee Leaves 
class EmployeeLeave(models.Model):
    STATUS_CHOICES = [
        ('APPROVED', 'Approved'),
        ('PENDING', 'Pending'),
        ('REJECTED', 'Rejected'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_id = models.CharField(max_length=50)
    leave_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.PositiveIntegerField()  # Duration in days, for example
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.employee} - {self.leave_type}"

class Salary(models.Model):
    EMPLOYEE_SALARY_TYPES = [
        ('Semi', 'Semi-Monthly'),
        ('Monthly', 'Monthly'),
        ('Hourly', 'Hourly'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_type = models.CharField(max_length=20, choices=EMPLOYEE_SALARY_TYPES)
    basic_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employee} - {self.salary_type}"


class Contract(models.Model):
    CONTRACT_TYPE_CHOICES = [
        ('FT', 'Full-Time'),
        ('PT', 'Part-Time'),
        ('CT', 'Contract'),
        ('TP', 'Temporary'),
        ('IT', 'Internship'),
    ]

    id = models.AutoField(primary_key=True)
    contract_type = models.CharField(max_length=2, choices=CONTRACT_TYPE_CHOICES)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
     
    def __str__(self):
        return f'{self.get_contract_type_display()} - {self.from_date} to {self.to_date}'