from django import template
register = template.Library()
from expense.models import *
from django.contrib.auth import get_user_model
from django.db.models.aggregates import Sum, Avg
from datetime import datetime
User = get_user_model()
c_m = datetime.now().month

@register.filter(name='get_percentage')
def get_used_budget_percentage(id, user_id):
    budget = Budget.objects.get(id=id)
    user = User.objects.get(id=user_id)

    if budget.duration == 'M':
        spendings = Spending.objects.filter(user=user, budget=budget, created_at__month=c_m)
        total_spent = spendings.aggregate(Sum('amount'))['amount__sum'] if spendings else 0
        percent = (total_spent * 100) / budget.amount
    return percent


@register.filter(name='get_date')
def get_date(value):
    if value.strftime('%Y-%m-%d') == datetime.today().strftime('%Y-%m-%d'):
        return value.strftime('%H:%M')
    else:
        return value.strftime('%d-%m-%Y')
    
@register.filter(name='base_value')
def get_base_value(value):
    return round(value)