from django import template
register = template.Library()
from expense.models import *
from django.contrib.auth import get_user_model
from django.db.models.aggregates import Sum, Avg

User = get_user_model()

@register.filter(name='get_percentage')
def get_used_budget_percentage(id, user_id):
    budget = Budget.objects.get(id=id)
    user = User.objects.get(id=user_id)

    if budget.duration == 'M':
        spendings = Spending.objects.filter(user=user, budget=budget)
        total_spent = spendings.aggregate(Sum('amount'))['amount__sum'] if spendings else 0
        percent = (total_spent * 100) / budget.amount
    return percent
