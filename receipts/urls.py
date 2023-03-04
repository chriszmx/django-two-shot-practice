from django.urls import path
from receipts.views import (receipt,
                            )


urlpatterns = [
    path('', receipt, name='home'),
]
