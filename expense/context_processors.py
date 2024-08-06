from .models import *
from django.db.models.aggregates import Sum, Avg
from datetime import datetime
from .utils import *



c_m = datetime.now().month
def get_expense_data(request):
    return {
        'total_spent_month' : get_total_month(request),
        'total_spent_today' : get_total_today(request),
        'total_spent_yesterday' : get_total_yesterday(request),
        'today' : get_today_date(),
    }