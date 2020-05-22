from django.urls import path

from .views import OrderListView, order_detail, payment_list, SearchResultsView
from .views import add_note, add_order, change_order, add_work, add_payment
from .views import generate_pdf, PdfView, generate_pdf_wp
from .views import settings_view

app_name = 'main'
urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search'),
    path('settings/', settings_view, name='settings-view'),
    path('printweasyprint/<int:pk>/', generate_pdf_wp, name='generate-pdf-wp'),
    path('printWP/<int:pk>/', PdfView.as_view(), name='generate-pdf-ws'),
    path('print/<int:pk>/', generate_pdf, name='generate-pdf'),
    path('add-payment/', add_payment, name='add-payment'),
    path('add-work/', add_work, name='add-work'),
    path('change-order/', change_order, name='change-order'),
    path('add-note/', add_note, name='add-note'),
    path('add-order/', add_order, name='add-order'),
    path('detail/<int:pk>/', order_detail, name='order-detail'),
    path('payments/', payment_list, name='payment-list'),
    path('', OrderListView.as_view(), name='index'),
]
