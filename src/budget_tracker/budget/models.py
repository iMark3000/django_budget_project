from django.db import models


# ACCOUNT RELATED MODELS
class FinancialAccount(models.Model):
    """Representation of financial accounts"""
    pass


class MonthlyAccountStatement(models.Model):
    """Representation of Monthly statements.
    Has a starting balance, and all transactions for the month deduct from it"""
    pass


#  TIME RELATED MODELS
class FiscalYear(models.Model):
    """Fiscal Year."""
    pass


class FiscalMonth(models.Model):
    """FiscalMonth is the core of the monthly budgets through the
    MonthlyBudgetExpenseItem and MonthlyBudgetIncomeItem models."""
    pass


#  EXPENSE RELATED MODELS
class ExpenseItem(models.Model):
    """Representation of expense transactions"""
    pass


class MonthlyBudgetExpenseItem(models.Model):
    """Representation of a line item on a monthly budget (i.e. budget $200 for gas)"""
    pass


class BudgetExpenseItem(models.Model):
    """A more high level representation of budget line items (i.e. gas, groceries, water bill).
    Purpose of this model is to standardize MonthlyBudgetExpenseItems and for use in queries."""
    pass


class BudgetExpenseCategory(models.Model):
    """An even more general model than BudgetExpenseItem.
    Categories for items such as bills, utilities general budget. Useful for reporting"""
    pass


class AmortizedBudgetItem(models.Model):
    """A way to amortize the cost of a big ticket purchase over multiple months.
    On the same level as BudgetExpenseItem"""
    pass


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
