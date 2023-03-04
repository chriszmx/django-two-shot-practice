from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt


# Create your views here.
@login_required
def receipt(request):
    receipts = Receipt.objects.all()
    context = {
        'receipts': receipts,
    }
    return render(request, 'receipts/receipt.html', context)
