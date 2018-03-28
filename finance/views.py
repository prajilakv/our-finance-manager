from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.views.generic import FormView

from .forms import AddIncomeDetailForm, AddPaymentForm, AddExpenseForm, AddExpenditureForm
from .models import IncomeDetail, Income, Payment, Expense, Expenditure

from django.contrib import messages
# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')

#### INCOME ###


# Income home (view)
@login_required
def view_income(request):
    total_income = Income.objects.filter()
    context = {"total_income": total_income}
    return render(request, 'income/income.html', context)

# add a new Incomedetail
@login_required
def add_income_detail(request):
    if request.method == 'POST':
        add_income_detail_form = AddIncomeDetailForm(data=request.POST)
        if add_income_detail_form.is_valid():
            income_detail = add_income_detail_form.save(commit=False)
            income_detail.user = request.user
            income_detail.save()
            messages.success(request, 'Payment option added successfully')
            add_income_detail_form = AddIncomeDetailForm(instance=request.user)
        else:
            messages.error(request, 'error')
    else:
        add_income_detail_form = AddIncomeDetailForm(instance=request.user)
    context = {'add_income_detail_form': add_income_detail_form}
    return render(request, 'income/add_income_detail.html', context)

#### PAYMENT ###


# Payment home (view)
@login_required
def view_payment_options(request):
    all_payment_options = Payment.objects.all()
    context = {"all_payment_options": all_payment_options}
    return render(request, 'payments/payment_options.html', context)


# add a new payment option
@login_required
def add_payment_option(request):
    if request.method == 'POST':
        add_payment_form = AddPaymentForm(data=request.POST)
        if add_payment_form.is_valid():
            payment = add_payment_form.save(commit=False)
            payment.user = request.user
            payment.save()
            messages.success(request, 'Payment option added successfully')
            add_payment_form = AddPaymentForm(instance=request.user)
        else:
            messages.error(request, 'error')
    else:
        add_payment_form = AddPaymentForm(instance=request.user)
    context = {'add_payment_form': add_payment_form}
    return render(request, 'payments/add_payment.html', context)


# Edit payment option
@login_required
def edit_payment_option(request, pk):
    selected_payment = Payment.objects.get(pk=pk)
    if request.method == 'POST':
        edit_payment_form = AddPaymentForm(data=request.POST, instance=selected_payment)
        if edit_payment_form.is_valid():
            edit_payment_form.save()
            messages.success(request, 'Payment option updated successfully')
            return redirect('payments')
        else:
            messages.error(request, "Payment update failed")
    else:
        edit_payment_form = AddPaymentForm(instance=selected_payment)
    context = {'edit_payment_form': edit_payment_form}
    return render(request, 'payments/edit_payment.html', context)


#### EXPENSE ###

# Expense home/ view expense
@login_required
def view_expense(request):
    all_expense = Expense.objects.all()
    context = {"all_expense": all_expense}
    return render(request, 'expense/view_expense.html', context)


# Add new expense
@login_required
def add_expense(request):
    if request.method == 'POST':
        add_expense_form = AddExpenseForm(data=request.POST)
        if add_expense_form.is_valid():
            expense = add_expense_form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully')
            add_expense_form = AddExpenseForm(instance=request.user)
        else:
            messages.error(request, 'error')
    else:
        add_expense_form = AddExpenseForm(instance=request.user)
    context = {'add_expense_form': add_expense_form}
    return render(request, 'expense/add_expense.html', context)


# Edit expense
@login_required
def edit_expense(request, pk):
    selected_expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        edit_expense_form = AddExpenseForm(data=request.POST, instance=selected_expense)
        if edit_expense_form.is_valid():
            edit_expense_form.save()
            messages.success(request, 'Expense updated successfully')
            return redirect('expenses')
        else:
            messages.error(request, "Expense update failed")
    else:
        edit_expense_form = AddExpenseForm(instance=selected_expense)
    context = {'edit_expense_form': edit_expense_form}
    return render(request, 'expense/edit_expense.html', context)


#### EXPENSE ITEM ###

# Expenditure home/ view Expenditure
@login_required
def view_expenditure(request):
    all_expenditure = Expenditure.objects.all()
    context = {"all_expenditure": all_expenditure}
    return render(request, 'expense/templates/expenditure/view_expenditure.html', context)


# Add new expenditure
@login_required
def add_expenditure(request):
    if request.method == 'POST':
        add_expenditure_form = AddExpenditureForm(data=request.POST)
        if add_expenditure_form.is_valid():
            expenditure = add_expenditure_form.save(commit=False)
            expenditure.user = request.user
            expenditure.save()
            messages.success(request, 'Expenditure added successfully')
            add_expenditure_form = AddExpenditureForm(instance=request.user)
        else:
            messages.error(request, 'error')
    else:
        add_expenditure_form = AddExpenditureForm(instance=request.user)
    context = {'add_expenditure_form': add_expenditure_form}
    return render(request, 'expense/templates/expenditure/add_expenditure.html', context)


# Edit expenditure
@login_required
def edit_expenditure(request, pk):
    selected_expenditure = Expenditure.objects.get(pk=pk)
    if request.method == 'POST':
        edit_expenditure_form = AddExpenditureForm(data=request.POST, instance=selected_expenditure)
        if edit_expenditure_form.is_valid():
            edit_expenditure_form.save()
            messages.success(request, 'Expense item updated successfully')
            return redirect('expenditures')
        else:
            messages.error(request, "Expenditure update failed")
    else:
        edit_expenditure_form = AddExpenditureForm(instance=selected_expenditure)
    context = {'edit_expenditure_form': edit_expenditure_form}
    return render(request, 'expense/templates/expenditure/edit_expenditure.html', context)


