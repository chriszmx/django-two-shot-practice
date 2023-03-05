from django.urls import path
from receipts.views import (receipt,
                            create_receipt,
                            category_list,
                            account_list,
                            create_category)


urlpatterns = [
    path('categories/create/', create_category, name='create_category'),
    path('accounts/', account_list, name='account_list'),
    path('categories/', category_list, name='category_list'),
    path('create/', create_receipt, name='create_receipt'),
    path('', receipt, name='home'),
]
