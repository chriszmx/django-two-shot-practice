from django.db import models
from django.conf import settings
# Create your models here.
# need to import django.conf import settings for AUTH_USER_MODEL


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='categories')

    def __str__(self):
        return self.name

# def __str__ function is allowing us to see the info in the data base
# with a name instead of object


class Account(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='accounts')

    def __str__(self):
        return self.name


class Receipt(models.Model):
    vendor = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    tax = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateTimeField(auto_now_add=True)
    purchaser = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name='receipts')
    category = models.ForeignKey(ExpenseCategory,
                                 on_delete=models.CASCADE,
                                 related_name='receipts',
                                 null=True)
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='receipts',
                                null=True)
