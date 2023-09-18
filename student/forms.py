from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import *


class add_student_form(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'Photo':forms.FileInput(attrs={'class':'form-control'}),
            'Name':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Enter Name'}),
            'Enrollment_No':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Enrollment No'}),
            'Course':forms.Select(attrs={'class':'form-control'}),
            'Gender':forms.Select(attrs={'class':'form-control'}),
            'Caste':forms.Select(attrs={'class':'form-control'}),
            'Father_Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Father Name'}),
            'Mother_Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mother Name'}),
            'Contact_No':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Contact No'}),
            'Email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}),
            'District':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter District Name'}),
            'Address':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Address','rows':'3'}),
            'Highest_Qualification':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Highest Qualification'}),
            'Name_Of_School':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name of the School'}),
            'Name_Of_Board':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name of the Board'}),
            'Year_Of_Pass':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Passing Year'}),
            'Marks_Obtained':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Marks Obtained'}),
            'DOB': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'Date_Of_Admission': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'Total_Fees': forms.HiddenInput(),
        }


class pay_installment_form(ModelForm):
    class Meta:
        model = Fees_Payment
        fields = '__all__'
        # exclude = ('Student',)

        widgets = {
            'Date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'Emi': forms.TextInput(attrs={'type': 'number' ,'class':'form-control'}),
            'Remarks': forms.Select(attrs={'class':'form-control'}),
            'Status': forms.Select(attrs={'class':'form-control'}),
            'Receiver': forms.Select(attrs={'class':'form-control'}),

            'Student':forms.HiddenInput(),
            'Due':forms.HiddenInput(),
        }


class add_show_fees_form(ModelForm):
    class Meta:
        model = Fees_Show
        fields = '__all__'
        # exclude = ('Student',)

        widgets = {
            'Emi_Payment_Date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),

            'Remarks': forms.Select(attrs={'class':'form-control'}),
            'Amount': forms.TextInput(attrs={'class':'form-control'}),

            'Student':forms.HiddenInput(),
        }

        
class add_courses_form(ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.CharField(widget=CKEditorWidget()),
            'Duration': forms.TextInput(attrs={'class':'form-control'}),
            'Eligibility': forms.TextInput(attrs={'class':'form-control'}),
            'Course_Fees': forms.TextInput(attrs={'class':'form-control'}),
            'Admission_Fee': forms.TextInput(attrs={'class':'form-control'}),
            'Fees_Structure': forms.TextInput(attrs={'class':'form-control'}),
        }


class add_enquries_form(ModelForm):
    class Meta:
        model = Enquries
        fields = '__all__'

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Course_Interest': forms.Select(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class':'form-control'}),
            'Mobile_No': forms.TextInput(attrs={'class':'form-control'}),
            'Whatsapp_No': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}),
            'Remarks': forms.TextInput(attrs={'class':'form-control'}),
        }
        

class Transaction_form(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

        widgets = {
            'Date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'Purpose': forms.Textarea(attrs={'class': 'form-control','rows':'1'}),
            'P_method': forms.Select(attrs={'help-text':'Payment Type','class':'form-control'}),
            'Amount':forms.TextInput(attrs={'class':'form-control'}),
        }
        
