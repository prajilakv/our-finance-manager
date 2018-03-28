from django import forms
# from django.conf import settings

# from django.contrib.auth.models import User
from .models import Payment, IncomeDetail, Expense, Expenditure


class AddPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['method', 'name', 'status']


class AddIncomeDetailForm(forms.ModelForm):
    class Meta:
        model = IncomeDetail
        fields = [ 'name', 'amount','type']


class AddExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['type', 'category', 'subcategory']


class AddExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ['expense', 'date', 'name', 'amount', 'payment']
