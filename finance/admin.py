from django.contrib import admin

from .models import Payment, Expense, Expenditure
# Register your models here.

admin.site.register(Payment)
admin.site.register(Expense)
admin.site.register(Expenditure)