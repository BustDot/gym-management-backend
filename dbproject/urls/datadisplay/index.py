from django.urls import path
from dbproject.views.datadisplay.data_display import DataDisplayView
from dbproject.views.datadisplay.list_balance_order import ListBalanceOrderView


urlpatterns = [
    path('', DataDisplayView.as_view(), name='data_display'),
    path('balanceorder/', ListBalanceOrderView.as_view(), name='balance_display'),

]