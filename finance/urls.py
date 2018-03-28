from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views as finance_views

urlpatterns = [
    url(r'^', include('user_Registration.urls')),
    url(r'^dashboard/$', finance_views.dashboard, name='dashboard'),
    # Payments
    url(r'^payments/$', finance_views.view_payment_options, name='payments'),
    url(r'^add-payment/$', finance_views.add_payment_option, name='add-payment'),
    url(r'^edit-payment/(?P<pk>[0-9]+)/$', finance_views.edit_payment_option, name='edit-payment'),

    # Expense
    url(r'^expense/$', finance_views.view_expense, name='expenses'),
    url(r'^add-expense/$', finance_views.add_expense, name='add-expense'),
    url(r'^edit-expense/(?P<pk>[0-9]+)/$', finance_views.edit_expense, name='edit-expense'),

    # Expense Items
    url(r'^expenditure/$', finance_views.view_expenditure, name='expenditures'),
    url(r'^add-expenditure/$', finance_views.add_expenditure, name='add-expenditure'),
    url(r'^edit-expenditure/(?P<pk>[0-9]+)/$', finance_views.edit_expenditure, name='edit-expenditure'),

]
