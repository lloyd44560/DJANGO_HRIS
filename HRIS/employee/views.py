from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.models import User  # Import the User model if needed
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse
from .forms import EmployeeForm, BankInformationForm, SalaryForm, ContractForm, DocumentForm
from .models import Employee, BankInformation, Salary, Contract, Document
from cities_light.models import Country


@login_required
def index(request):
    context = {
        'title': 'Django Templates',
        'message': 'This is a sample page using Django templates.'
    }
    return render(request, 'admin/dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(f"Email: {email}, Password: {password}")  
        
        user = authenticate(request, username=email, password=password)
        print("User object:", user) 

        if user is not None:
            login(request, user)
          
            if user.is_superuser:
                return redirect('admin_dashboard')  
            else:
                return redirect('user_dashboard')  
        else:
            # Authentication failed, show error message
            error_message = "Invalid email or password. Please try again."
            print("Invalid email or password. Please try again.")  # Debugging statement
            return render(request, 'Login.html', {'error_message': error_message})
    else:
        return render(request, 'Login.html')



def pagelogout(request):
    logout(request)
    return redirect('/login')


def manage_employee(request):
    employees = Employee.objects.all() 
    countries = Country.objects.all()   
    employee_form = EmployeeForm()
    bank_info_form = BankInformationForm()
    salary_form = SalaryForm()
    contract_form = ContractForm()
    document_form = DocumentForm()

    return render(request, 'admin/employee.html', {'employees': employees,'employee_form': employee_form,  'bank_info_form': bank_info_form, 'country_list': countries, 'salary_form': salary_form, 'contract_form'  : contract_form , 'document_form' : document_form})




def add_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        bank_info_form = BankInformationForm(request.POST)
        salary_form = SalaryForm(request.POST)
        contract_form = ContractForm(request.POST)
        document_form = DocumentForm(request.POST)
        if employee_form.is_valid() and bank_info_form.is_valid()  and salary_form.is_valid() and contract_form.is_valid() and document_form.is_valid() :
            # Save the Employee record
            employee_instance = employee_form.save()

            # Create BankInformation instance and associate with Employee
            bank_info_instance = bank_info_form.save(commit=False)
            bank_info_instance.employee = employee_instance
            bank_info_instance.save()

            # Create Salary instance and associate with Employee
            salary_instance = salary_form.save(commit=False)
            salary_instance.employee = employee_instance
            salary_instance.save()


            contract_instance = contract_form.save(commit=False)
            contract_instance.employee = employee_instance
            contract_instance.save()

            
            document_instance = document_form.save(commit=False)
            document_instance.employee = employee_instance
            document_instance.save()
            return JsonResponse({'success': True})
        
        else:
            errors = {}
            errors.update(employee_form.errors)
            errors.update(bank_info_form.errors)
            errors.update(salary_form.errors)
            errors.update(contract_form.errors)
            errors.update(document_form.errors)

            return JsonResponse({'success': False, 'errors': errors})
      
    else:
        employee_form = EmployeeForm()
        bank_info_form = BankInformationForm()
        salary_form = SalaryForm()
        contract_form = ContractForm()
        document_form = DocumentForm()

    return render(request, 'add_employee.html', {'employee_form': employee_form, 'bank_info_form': bank_info_form, 'salary_form': salary_form , 'contract_form' : contact_form , 'document_form' : document_form})



# def add_employee(request):
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST, request.FILES)
#         if form.is_valid():
#             employee = form.save(commit=False)
#             employee.save()
                
#             # employee_id = request.POST.get('employee_id')
#             # first_name = request.POST.get('first_name')
#             # middle_name = request.POST.get('middle_name')
#             # last_name = request.POST.get('last_name')
#             # suffix = request.POST.get('suffix')
#             # email = request.POST.get('email')   
#             # gender = request.POST.get('gender')   
#             # date_of_birth = request.POST.get('date_of_birth')   
#             # place_of_birth = request.POST.get('place_of_birth')   
#             # age = request.POST.get('age')  
#             # contact_number = request.POST.get('contact_number')  
#             # religion = request.POST.get('religion')  
#             # civil_status = request.POST.get('civil_status')  
#             # barangay = request.POST.get('barangay')  
#             # city = request.POST.get('city')
#             # house_number = request.POST.get('house_number')
#             # country = request.POST.get('country')
#             # zip = request.POST.get('zip')
#             # tin = request.POST.get('tin')
#             # country_field = request.POST.get('country_field')
#             # country_instance = get_object_or_404(Country, pk=country_field)
#             # image =  request.FILES.get('image')
#             # image_file = request.FILES.get('image')
#             # if image_file:
#             #     print(f"Received image file: {image_file.name}")
#             # else:
#             #     print("No image file received")

#             # if not employee_id or not first_name or not last_name or not email:
#             #     return JsonResponse({'success': False, 'errors': 'Required fields are missing'})
#             # if image:
#             #     print("LAMAN NG IMAGE", image)
#             # else: print('WALA LAMAN IMAGE')
#             # # Create and save the new employee
#             # employee = Employee(
#             #     employee_id=employee_id,
#             #     first_name=first_name,
#             #     middle_name=middle_name,
#             #     last_name=last_name,
#             #     suffix=suffix,
#             #     email=email,
#             #     gender = gender,
#             #     date_of_birth = date_of_birth,
#             #     place_of_birth = place_of_birth,
#             #     age = age, 
#             #     contact_number = contact_number, 
#             #     religion = religion,  
#             #     civil_status = civil_status,  
#             #     barangay = barangay,
#             #     city = city, 
#             #     house_number = house_number,
#             #     country = country,
#             #     zip = zip,
#             #     tin = tin,
#             #     country_field = country_instance,
#             #     image = image,

#             # )


#             # employee.save()


#             # Bank information
#             bank_holder_name = request.POST.get('bank_holder_name')
#             bank_name = request.POST.get('bank_name')
#             branch = request.POST.get('branch')
#             account_number = request.POST.get('account_number')
#             account_type = request.POST.get('account_type')

#             bank_info = BankInformation(
#                 employee=employee,  # Use the 'employee' object here
#                 bank_holder_name=bank_holder_name,
#                 bank_name=bank_name,
#                 branch=branch,
#                 account_number=account_number,
#                 account_type=account_type
#             )

#             bank_info.save()
            
#             # Salary Information
#             salary_type = request.POST.get('salary_type')
#             basic_pay = request.POST.get('basic_pay')

#             salary_info = Salary(
#                 employee=employee, 
#                 salary_type=salary_type,
#                 basic_pay=basic_pay

#             )
#             salary_info.save()

            
#             # Contract Information 




#             return JsonResponse({'success': True})

#     return JsonResponse({'success': False, 'errors': 'Invalid request method'})


def edit_employee(request, employee_id):

    employee = get_object_or_404(Employee, id=employee_id)
    # Retrieve other related information like bank info, salary info, etc.
    # Pass the employee object and related information to the template

    print("NATATAWAG AKO BOSS")
    return render(request, 'admin/edit_employee.html', {'employee': employee})


def retrieve_employee_info(request):
    if request.method == 'GET':
        print("Natatawag bako ng maayus ?")
        
        # Get the employee ID from the request parameters
        employee_id = request.GET.get('employee_id')
        print(employee_id, "Employee ID boss")

        try:
            # Query the database to retrieve the employee's information
            employee = Employee.objects.get(employee_id=employee_id)
            bank_info = BankInformation.objects.get(employee_id=employee_id)
            country_list = Country.objects.all()  # Fetch all countries

            if employee:
                print("KITA KA")
            else:
                print("DI MAKITA")
            if country_list:
                print("BRO MAY COUNTRY")
            else:
                print("WALA COUNTRY")
            if bank_info:
                print("May bank info")

            employee_info = {
                'employee_id': employee.employee_id,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'middle_name': employee.middle_name,
                'suffix': employee.suffix,
                'email': employee.email,
                'date_of_birth': employee.date_of_birth.strftime('%Y-%m-%d') if employee.date_of_birth else "",
                'place_of_birth': employee.place_of_birth,
                'gender': employee.gender,
                'age': employee.age,
                'contact_number': employee.contact_number,
                'barangay': employee.barangay,
                'city': employee.city,
                'house_number': employee.house_number,
                'country_id': employee.country_field.pk if employee.country_field else None,
                'zip': employee.zip,
                'tin': employee.tin,
                'image' : employee.image,
            }

            bank_info_data = {
                'bank_holder_name': bank_info.bank_holder_name,
                'bank_name': bank_info.bank_name,
                'branch': bank_info.branch,
                'account_number': bank_info.account_number,
                'account_type': bank_info.account_type,
            }

          # Return the employee and bank information as JSON response
            return JsonResponse({'success': True, 'employee_info': employee_info, 'bank_info': bank_info_data, 'country_list': list(country_list.values('pk', 'name'))})


        except Employee.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Employee not found'})

    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})



@login_required
def update_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('editEmployeeId')
        employee = get_object_or_404(Employee, employee_id=employee_id)
        
        employee.first_name = request.POST.get('editFirstName')
        employee.middle_name = request.POST.get('editMiddleName')
        employee.last_name = request.POST.get('editLastName')
        employee.suffix = request.POST.get('editSuffix')
        employee.email = request.POST.get('editEmail')
        employee.gender = request.POST.get('editGender')
        employee.date_of_birth = request.POST.get('editDateOfBirth')
        employee.place_of_birth = request.POST.get('editPlaceOfBirth')
        employee.age = request.POST.get('editAge')
        employee.contact_number = request.POST.get('editContactNumber')
        # employee.religion = request.POST.get('religion')
        # employee.civil_status = request.POST.get('civil_status')
        employee.barangay = request.POST.get('editBarangay')
        employee.city = request.POST.get('editCity')
        employee.house_number = request.POST.get('editHouseNumber')
        employee.zip = request.POST.get('editZip')
        employee.tin = request.POST.get('editTin')
        country_id = request.POST.get('country_field')
        employee.country_field = get_object_or_404(Country, pk=country_id)
        
        employee.save()

        # # Update Bank Information
        # bank_info = BankInformation.objects.get(employee=employee)
        # bank_info.bank_holder_name = request.POST.get('bank_holder_name')
        # bank_info.bank_name = request.POST.get('bank_name')
        # bank_info.branch = request.POST.get('branch')
        # bank_info.account_number = request.POST.get('account_number')
        # bank_info.account_type = request.POST.get('account_type')
        # bank_info.save()

        # # Update Salary Information
        # salary_info = Salary.objects.get(employee=employee)
        # salary_info.salary_type = request.POST.get('salary_type')
        # salary_info.basic_pay = request.POST.get('basic_pay')
        # salary_info.save()

        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': 'Invalid request method'})