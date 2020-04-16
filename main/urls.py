from django.urls import path

from .views import OrderListView, order_detail, payment_list
from .views import add_note, add_order, change_order, add_work, add_payment
from .views import generate_pdf

app_name = 'main'
urlpatterns = [
    path('print/<int:pk>', generate_pdf, name='generate-pdf'),
    path('add-payment/', add_payment, name='add-payment'),
    path('add-work/', add_work, name='add-work'),
    path('change-order/', change_order, name='change-order'),
    path('add-note/', add_note, name='add-note'),
    path('add-order/', add_order, name='add-order'),
    path('detail/<int:pk>/', order_detail, name='order-detail'),
    path('payments/', payment_list, name='payment-list'),
    path('', OrderListView.as_view(), name='index'),
]
