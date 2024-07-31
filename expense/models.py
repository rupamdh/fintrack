from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Budget(models.Model):
    DURATION_CHOICE = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
    )
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.CharField(max_length=2, choices=DURATION_CHOICE, default='M')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "budgets"

        

class Spending(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spending_user')
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='spending_budget')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.amount} - {self.note}"
    
    class Meta:
        verbose_name_plural = "spendings"