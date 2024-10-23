from django import forms
from .models import Student, LibraryHistory, FeesHistory

# Student Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'class_name', 'roll_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Library History Form
class LibraryHistoryForm(forms.ModelForm):
    class Meta:
        model = LibraryHistory
        fields = ['student', 'book_title', 'issue_date', 'return_date']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'book_title': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'return_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

# Fees History Form
class FeesHistoryForm(forms.ModelForm):
    class Meta:
        model = FeesHistory
        fields = ['student', 'amount_paid', 'date_paid']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_paid': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
