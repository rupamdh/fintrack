from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Budget, Spending
from django.contrib.auth import get_user_model
from .forms import SpendingForm, BudgetAddForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

User = get_user_model()
c_m = datetime.now().month
yesterday = datetime.now() - timedelta(1)

# Create your views here.
@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetAddForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('budget')
    else:
        form = BudgetAddForm()
    
    context = {
        'form' : form
    }
    return render(request, 'budget_add.html', context)

@login_required
def view_budgets(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'budget_list.html', {'budgets': budgets})

@login_required
def add_spending(request):
    if request.method == 'POST':
        form = SpendingForm(request.POST)
        if form.is_valid():
            spending = form.save(commit=False)
            spending.user = request.user
            spending.save()
            return redirect('spending-success')
    else:
        form = SpendingForm()

    context = {
        'form' : form,
    }
    return render(request, 'spending_add.html', context)

@login_required
def spending_add_success(request):
    return render(request,'spending_add_success.html')

@login_required
def view_spendings(request):
    today_spendings = Spending.objects.filter(user=request.user, created_at__date=datetime.today()).order_by('-created_at')
    yes_spendings = Spending.objects.filter(user=request.user, created_at__date=yesterday).order_by('-created_at')
    old_spendings = Spending.objects.filter(user=request.user, created_at__date__lt=yesterday).order_by('-created_at')
    context = {
        'today_spendings' : today_spendings,
        'yes_spendings' : yes_spendings,
        'old_spendings' : old_spendings
    }
    return render(request, 'spending_list.html', context)

@login_required
def get_timely_expense(request):
    filter = request.POST.get('filter')
    print(filter)
    return JsonResponse({'success': True})
