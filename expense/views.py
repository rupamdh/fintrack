from django.shortcuts import render, redirect
from .models import Budget, Spending
from django.contrib.auth import get_user_model
from .forms import SpendingForm

User = get_user_model()
# Create your views here.
def add_budget(request):
    if request.method == 'POST':
        Budget.objects.create(
            name=request.POST['name'],
            user = request.user,
            amount=request.POST['amount']
        )
        return redirect('home')
    return render(request, 'budget_add.html')

def view_budgets(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'budget_list.html', {'budgets': budgets})

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
