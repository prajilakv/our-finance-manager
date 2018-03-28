from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# model to save income information in detail
# model to save income information in detail
TYPE_CHOICES = (
    ('O', 'Onetime'),
    ('C', 'Recur'),
)

VALIDITY_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
)


class IncomeDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='O')
    validity = models.CharField(max_length=2, choices=TYPE_CHOICES, default='Y')

    def __str__(self):
        return self.name


# model to save total income month wise

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=8, decimal_places=2)
    period = models.DateTimeField()


# model to save payment options of the user(account,credit card names etc)
PAYMENT_CHOICES = (
    ('A', 'Account'),
    ('C', 'Credit'),
)

STATUS_CHOICES = (
    ('A', 'Active'),
    ('I', 'Inactive'),
)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.CharField(max_length=2, choices=PAYMENT_CHOICES, default='A')
    name = models.CharField(max_length=150, unique=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='A')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# model to save structure of expenses
class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


# model to save each expense details
class Expenditure(models.Model):
    expenditure_id = models.AutoField(primary_key=True)
    expense = models.ForeignKey(Expense, on_delete=models.PROTECT)
    date = models.DateTimeField()
    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
