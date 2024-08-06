from .models import *
from datetime import datetime, timedelta

def get_today_date():
    return datetime.now().strftime('%b %d %Y, %a')

def get_today_spendings(request):
    return Spending.objects.filter(user=request.user, created_at__date=datetime.now().date())

def get_total_today(request):
    today_spendings = get_today_spendings(request)
    return sum(spending.amount for spending in today_spendings)

def get_yesterday_spendings(request):
    yesterday = datetime.now() - timedelta(days=1)
    return Spending.objects.filter(user=request.user, created_at__date=yesterday.date())

def get_total_yesterday(request):
    yesterday_spendings = get_yesterday_spendings(request)
    return sum(spending.amount for spending in yesterday_spendings)

def get_week_spendings(request):
    today = datetime.now()
    week_start = today - timedelta(days=(today.weekday() or 7) - 1)
    return Spending.objects.filter(user=request.user, created_at__gte=week_start)

def get_total_week(request):
    week_spendings = get_week_spendings(request)
    return sum(spending.amount for spending in week_spendings)

def get_month_spendings(request):
    c_m = datetime.now().month
    return Spending.objects.filter(user=request.user, created_at__month=c_m)

def get_total_month(request):
    spendings_month = get_month_spendings(request)
    return sum(spending.amount for spending in spendings_month)

