from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt, ExpenseCategory,  Account
from receipts.forms import ReceiptForm, ExpenseCategoryForm, AccountForm


# Create your views here.
@login_required
def receipt(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        'receipts': receipts,
    }
    return render(request, 'receipts/receipt.html', context)


@login_required
def create_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect('home')
    else:
        form = ReceiptForm()
    context = {
        'form': form,
    }
    return render(request, 'receipts/create_receipt.html', context)


@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        'receipts': categories,
    }
    return render(request, 'receipts/category_list.html', context)


@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        'receipts': accounts,
    }
    return render(request, 'receipts/account_list.html', context)


@login_required
def create_category(request):
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect('category_list')
    else:
        form = ExpenseCategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'receipts/create_category.html', context)


@login_required
def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            account.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    context = {
        'form': form,
    }
    return render(request, 'receipts/create_account.html', context)
