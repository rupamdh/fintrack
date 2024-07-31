from django.shortcuts import render, redirect
from .models import Budget, Spending
from django.contrib.auth import get_user_model
from .forms import SpendingForm, BudgetAddForm
from django.contrib.auth.decorators import login_required

User = get_user_model()
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
            return redirect('home')
    else:
        form = SpendingForm()

    return render(request, 'spending_add.html', {'form' : form})
