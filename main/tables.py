import django_tables2 as tables

from .models import Order, CompletedWork, Payment


class OrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = "django_tables2/bootstrap.html"
        row_attrs = {
            "data-href": lambda record: record.get_absolute_url,
            "style": lambda record: "cursor: pointer;",
        }
        fields = ("id", "phone", "availability_date", "appearance", "executor", "device_type",
                  "brand", "model", "malfunction", "client_name",)


class WorkTable(tables.Table):
    class Meta:
        model = CompletedWork
        template_name = "django_tables2/bootstrap.html"
        fields = ("work", "amount", "price", "cost")


class PaymentTable(tables.Table):

    class Meta:
        model = Payment
        template_name = "django_tables2/bootstrap.html"
        fields = ("data", "description",  "total")


class PaymentListTable(tables.Table):
    class Meta:
        model = Payment
        template_name = "django_tables2/bootstrap.html"
        fields = ("order__id", "data", "description",  "total")
