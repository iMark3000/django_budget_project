from django.db import models


# ACCOUNT RELATED MODELS
class FinancialAccount(models.Model):
    """Representation of financial accounts"""
    name = models.CharField(max_length=200)


class MonthlyAccountStatement(models.Model):
    """Representation of Monthly statements.
    Has a starting balance, and all transactions for the month deduct from it"""
    pass


#  TIME RELATED MODELS
class FiscalYear(models.Model):
    """Fiscal Year."""
    year_id = models.IntegerField(primary_key=True)
    year_start_date = models.DateField(unique_for_year=True)
    year_end_date = models.DateField(unique_for_year=True)

    def __str__(self):
        return f'{self.year_id}'

    def __repr__(self):
        return f'Fiscal Year {self.year_id}'


class FiscalMonth(models.Model):
    """FiscalMonth is the core of the monthly budgets through the
    MonthlyBudgetExpenseItem and MonthlyBudgetIncomeItem models."""
    MONTH_CHOICES = [
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    ]

    month_id = models.IntegerField(primary_key=True)
    month_name = models.IntegerField(choices=MONTH_CHOICES)
    month_start_date = models.DateField()
    month_end_date = models.DateField()
    fiscal_year = models.ForeignKey("FiscalYear", on_delete=models.CASCADE)


#  EXPENSE RELATED MODELS
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100, unique=True)


class ExpenseItem(models.Model):
    """Representation of expense transactions"""
    transaction_date = models.DateField()
    amount = models.FloatField()
    description = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE, null=True)
    budget_expense_item = models.ForeignKey("MonthlyBudgetExpenseItem", on_delete=models.CASCADE, null=True)
    account = models.ForeignKey("FinancialAccount", on_delete=models.CASCADE, null=True)
    reference = models.CharField(unique=True)


class MonthlyBudgetExpenseItem(models.Model):
    """Representation of a line item on a monthly budget (i.e. budget $200 for gas)"""
    budget_item = models.ForeignKey("BudgetExpenseItem", on_delete=models.CASCADE, null=True)
    fiscal_month = models.ForeignKey("FiscalMonth", on_delete=models.CASCADE, null=True)
    amount = models.FloatField(blank=True, null=True)


class BudgetExpenseItem(models.Model):
    """A more high level representation of budget line items (i.e. gas, groceries, water bill).
    Purpose of this model is to standardize MonthlyBudgetExpenseItems and for use in queries."""
    item_category = models.ForeignKey("BudgetExpenseCategory", on_delete=models.CASCADE)
    item_name = models.CharField(unique=True, max_length=200)
    amortized_budget_item = models.ForeignKey("AmortizedBudgetItem", on_delete=models.CASCADE, null=True)


class BudgetExpenseCategory(models.Model):
    """An even more general model than BudgetExpenseItem.
    Categories for items such as bills, utilities general budget. Useful for reporting"""
    category_name = models.CharField(unique=True, max_length=200)


class AmortizedBudgetItem(models.Model):
    """A way to amortize the cost of a big ticket purchase over multiple months.
    On the same level as BudgetExpenseItem"""
    item_name = models.CharField(max_length=200)
    number_of_months = models.IntegerField()
    amount = models.FloatField()
    month_start = models.ForeignKey("FiscalMonth", on_delete=models.CASCADE)
    month_end = models.ForeignKey("FiscalMonth", on_delete=models.CASCADE)


#  INCOME RELATED MODELS
class IncomeItem(models.Model):
    """Representation of an income transaction"""
    pass


class MonthlyBudgetIncomeItem(models.Model):
    """Representation of a line item on a monthly budget for income (i.e. expect $2000 from FooBar Inc.)"""
    pass


class BudgetIncomeItem(models.Model):
    """A more high level representation of budget line items of income (i.e. paycheck, reimbursement).
    Purpose of this model is to standardize MonthlyBudgetIncomeItem and for use in queries."""
    pass


class BudgetIncomeCategory(models.Model):
    """An even more general model than BudgetIncomeItem. Probably not as useful as it's expense counterpart"""
    pass
