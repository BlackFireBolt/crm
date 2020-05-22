from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from datatableview.views import DatatableView
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize
import json
from django.conf import settings
from django.template.loader import render_to_string
import weasyprint
import tempfile
import django_tables2 as tables
from django.contrib.postgres.search import SearchVector
from django_tables2 import SingleTableView, LazyPaginator
from django_weasyprint import WeasyTemplateResponseMixin
from django.template import Template, Context, RequestContext

from .utils import render_to_pdf
from .models import Order, Comment, Note, CompletedWork, Payment
from .models import Settings, PdfTemplate, AdditionalImage
from .tables import OrderTable, WorkTable, PaymentTable, PaymentListTable
from .forms import OrderForm, NoteForm, CompletedWorkForm, IncomeFormList, ConsumptionFormList, IncomeForm
from .forms import ConsumptionForm
from .forms import PdfTemplateForm


class OrderListView(SingleTableView):
    model = Order
    table_class = OrderTable
    paginator_class = LazyPaginator
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['form'] = OrderForm()
        return context


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_form = OrderForm(instance=order)
    work_form = CompletedWorkForm()
    note_form = NoteForm()
    income_form = IncomeForm()
    consumption_form = ConsumptionForm()
    notes = Note.objects.all()
    work_table = WorkTable(CompletedWork.objects.filter(order=pk))
    payment = Payment.objects.filter(order=pk)
    payment_table = PaymentTable(payment)
    total = 0
    for pay in payment:
        if pay.type == 'c':
            total -= pay.total
        elif pay.type == 'i':
            total += pay.total
    context = {'order': order, 'order_form': order_form, 'note_form': note_form, 'notes': notes,
               'work_form': work_form, 'work_table': work_table, 'payment_table': payment_table,
               'income_form': income_form, 'consumption_form': consumption_form, 'total': total}
    return render(request, 'main/order_detail.html', context)


def add_order(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        phone = request.POST.get('phone')
        if request.POST.get('quickly') == 'on':
            quickly = True
        else:
            quickly = False
        device_type = request.POST.get('device_type')
        serial_number = request.POST.get('serial_number')
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        equipment = request.POST.get('equipment')
        appearance = request.POST.get('appearance')
        password = request.POST.get('password')
        malfunction = request.POST.get('malfunction')
        receiver_notes = request.POST.get('receiver_notes')
        indicative_price = request.POST.get('indicative_price')
        executor = request.POST.get('executor')
        prepayment = request.POST.get('prepayment')
        availability_date = request.POST.get('availability_date')

        response_data = {}

        order = Order(client_name=client_name, phone=phone, quickly=quickly, device_type=device_type,
                      brand=brand, model=model, equipment=equipment, appearance=appearance, password=password,
                      malfunction=malfunction, receiver_notes=receiver_notes, indicative_price=indicative_price,
                      executor=executor, prepayment=prepayment, serial_number=serial_number,
                      availability_date=availability_date)
        order.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = order.pk
        response_data['client_name'] = client_name
        response_data['phone'] = phone
        response_data['quickly'] = quickly
        response_data['device_type'] = device_type
        response_data['serial_number'] = serial_number
        response_data['brand'] = brand
        response_data['model'] = model
        response_data['equipment'] = equipment
        response_data['appearance'] = appearance
        response_data['password'] = password
        response_data['malfunction'] = malfunction
        response_data['receiver_notes'] = receiver_notes
        response_data['indicative_price'] = indicative_price
        response_data['executor'] = executor
        response_data['prepayment'] = prepayment
        response_data['availability_date'] = availability_date
        response_data['flag'] = 0

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def add_note(request):
    if request.method == 'POST':
        orderpk = request.POST.get('orderpk')
        note_text = request.POST.get('note_data')
        note_t = request.POST.get('type')
        response_data = {}

        note_object = Note(order_id=orderpk, text=note_text, note_type=note_t)
        note_object.save()

        response_data['result'] = 'Create post successful!'
        response_data['note_text'] = note_text
        response_data['note_type'] = note_t
        response_data['orderpk'] = orderpk

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def change_order(request):
    if request.method == 'POST':
        orderpk = request.POST.get('orderpk')
        client_name = request.POST.get('client_name')
        phone = request.POST.get('phone')
        if request.POST.get('quickly') == 'on':
            quickly = True
        else:
            quickly = False
        device_type = request.POST.get('device_type')
        serial_number = request.POST.get('serial_number')
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        equipment = request.POST.get('equipment')
        appearance = request.POST.get('appearance')
        password = request.POST.get('password')
        malfunction = request.POST.get('malfunction')
        receiver_notes = request.POST.get('receiver_notes')
        indicative_price = request.POST.get('indicative_price')
        executor = request.POST.get('executor')
        prepayment = request.POST.get('prepayment')
        executor_note = request.POST.get('executor_note')
        verdict = request.POST.get('verdict')
        availability_date = request.POST.get('availability_date')

        response_data = {}

        order = Order.objects.get(pk=orderpk)
        order.client_name = client_name
        order.phone = phone
        order.quickly = quickly
        order.device_type = device_type
        order.serial_number = serial_number
        order.brand = brand
        order.model = model
        order.equipment = equipment
        order.appearance = appearance
        order.password = password
        order.malfunction = malfunction
        order.receiver_notes = receiver_notes
        order.indicative_price = indicative_price
        order.executor = executor
        order.prepayment = prepayment
        order.executor_note = executor_note
        order.verdict = verdict
        order.availability_date = availability_date

        order.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = order.pk
        response_data['client_name'] = client_name
        response_data['phone'] = phone
        response_data['quickly'] = quickly
        response_data['device_type'] = device_type
        response_data['serial_number'] = serial_number
        response_data['brand'] = brand
        response_data['model'] = model
        response_data['equipment'] = equipment
        response_data['appearance'] = appearance
        response_data['password'] = password
        response_data['malfunction'] = malfunction
        response_data['receiver_notes'] = receiver_notes
        response_data['indicative_price'] = indicative_price
        response_data['executor'] = executor
        response_data['prepayment'] = prepayment
        response_data['flag'] = 1
        response_data['availability_date'] = availability_date

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def add_work(request):
    if request.method == 'POST':
        order_pk = request.POST.get('order_pk')
        work = request.POST.get('work')
        amount = int(request.POST.get('amount'))
        price = int(request.POST.get('price'))
        cost = amount * price
        warranty = int(request.POST.get('warranty'))
        response_data = {}

        work_object = CompletedWork(order_id=order_pk, work=work, amount=amount, price=price,
                                    cost=cost, warranty=warranty)
        work_object.save()

        response_data['result'] = 'Create post successful!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def add_payment(request):
    if request.method == 'POST':
        order_pk = request.POST.get('order_pk')
        description = request.POST.get('description')
        total = int(request.POST.get('total'))
        payment_type = request.POST.get('type')
        response_data = {}

        payment_object = Payment(order_id=order_pk, description=description, total=total, type=payment_type)
        payment_object.save()

        response_data['result'] = 'Create post successful!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def payment_list(request):
    income_form = IncomeFormList()
    consumption_form = ConsumptionFormList()
    payment = Payment.objects.all()
    payment_list_table = PaymentListTable(payment)
    payment_list_table.paginate(page=request.GET.get('page', 1), per_page=25)
    total = 0
    for pay in payment:
        if pay.type == 'c':
            total -= pay.total
        elif pay.type == 'i':
            total += pay.total
    return render(request, 'main/payment_list.html', {'payment_list_table': payment_list_table,
                                                      'income_form': income_form, 'consumption_form': consumption_form,
                                                      'total': total})


def generate_pdf(request, pk):
    order_pdf = get_object_or_404(Order, id=pk)
    pdf = render_to_pdf('main/pdf.html', {'order': order_pdf, 'static': settings.STATIC_ROOT})
    return HttpResponse(pdf, content_type='application/pdf')


class PdfView(DetailView):
    model = Order
    template_name = 'main/pdf.html'


class MyModelPrintView(WeasyTemplateResponseMixin, PdfView):
    # output of MyModelView rendered as PDF with hardcoded CSS
    pdf_stylesheets = [
        settings.STATIC_ROOT + 'css/pdf.css',
        ]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False
    # suggested filename (is required for attachment!)
    pdf_filename = 'foo.pdf'


def generate_pdf_wp(request, pk):
    """Generate pdf."""
    # Model data
    order = get_object_or_404(Order, pk=pk)
    html_text = get_object_or_404(PdfTemplate, pk=1)
    # Rendered
    template = Template(html_text.pdf_text)
    work_table = WorkTable(CompletedWork.objects.filter(order=pk))
    image = get_object_or_404(AdditionalImage, pk=1)
    context = RequestContext(request, {'order': order, 'work_table': work_table, 'image': image})
    html_string = template.render(context)
    html = weasyprint.HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=order_pdf.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response


def settings_view(request):
    settings_obj = get_object_or_404(Settings, pk=1)
    pdf_form = PdfTemplateForm()
    return render(request, 'main/settings_view.html', {'settings_obj': settings_obj, 'pdf_form': pdf_form})


class SearchResultsView(SingleTableView):
    model = Order
    template_name = 'main/search.html'
    table_class = OrderTable
    paginator_class = LazyPaginator

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_vector = SearchVector()
        object_list = Order.objects.annotate(search=search_vector).filter(search=query)
        return object_list
