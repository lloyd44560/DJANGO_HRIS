from django import forms
from .models import Employee, BankInformation, Department , Salary, Contract, Document
from django_countries.widgets import CountrySelectWidget


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'middle_name', 'last_name', 'suffix', 'email','date_of_birth', 'place_of_birth', 
        'age', 'contact_number', 'religion', 'civil_status', 'barangay', 'city', 'house_number', 'country', 'country_field', 'zip', 'tin' , 'image']
        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control-file', 'accept': 'image/*'})

        self.fields['middle_name'].required = False
        self.fields['suffix'].required = False   
        self.fields['date_of_birth'].required = False   
        self.fields['place_of_birth'].required = False   
        self.fields['religion'].required = False   
        self.fields['civil_status'].required = False
        self.fields['barangay'].required = False  
        self.fields['city'].required = False   
        self.fields['house_number'].required = False  
        self.fields['country'].required = False 
        self.fields['country_field'].required = False  
        self.fields['zip'].required = False  
        self.fields['tin'].required = False  
        self.fields['image'].required = False  

    
class BankInformationForm(forms.ModelForm):
    class Meta:
        model = BankInformation
        fields = ['bank_holder_name', 'bank_name', 'branch', 'account_number', 'account_type']

    def __init__(self, *args, **kwargs):
        super(BankInformationForm, self).__init__(*args, **kwargs)
     

        self.fields['bank_holder_name'].required = False
        self.fields['bank_name'].required = False   
        self.fields['branch'].required = False   
        self.fields['account_number'].required = False   
        self.fields['account_type'].required = False   
       
class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['salary_type', 'basic_pay']
    
    def __init__(self, *args, **kwargs):
        super(SalaryForm, self).__init__(*args, **kwargs)

        self.fields['salary_type'].required = False
        self.fields['basic_pay'].required = False   

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields=['contract_type', 'description', 'from_date', 'to_date' ]

        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'to_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.DateInput(attrs={'type': 'text', 'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)

        self.fields['contract_type'].required = False
        self.fields['description'].required = False  
        self.fields['from_date'].required = False
        self.fields['to_date'].required = False  

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file_name', 'file_url']

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['file_name'].required = False
        self.fields['file_url'].required = False  
      