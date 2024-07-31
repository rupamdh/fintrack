from django import template
register = template.library()

from expense.models import *

@register.filter(name='get_percentage')
def get_used_budget_percentage(id, user_id):
    budget = Budget.objects.get(id=id)
    if budget.duration == 'D':
        spendings = Spending.objects.filter(user_id=user_id, budget=budget)