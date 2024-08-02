from .models import *
from django.db.models.aggregates import Sum, Avg
from datetime import datetime

c_m = datetime.now().month
def get_expense_data(request):
    spendings_month = Spending.objects.filter(user=request.user, created_at__month=c_m)
    total_spent_month = spendings_month.aggregate(Sum('amount'))['amount__sum'] if spendings_month else 0 
    spendings_today = Spending.objects.filter(user=request.user, created_at__date=datetime.today())
    total_spent_today = spendings_today.aggregate(Sum('amount'))['amount__sum'] if spendings_today else 0

    return {
        'total_spent_month' : total_spent_month,
        'total_spent_today' : total_spent_today
    }