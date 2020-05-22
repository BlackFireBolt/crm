from django.contrib import admin

from .models import Order, Comment, Note, CompletedWork, Payment
from .models import Settings, PdfTemplate, AdditionalImage

admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Note)
admin.site.register(CompletedWork)
admin.site.register(Payment)

admin.site.register(Settings)
admin.site.register(PdfTemplate)
admin.site.register(AdditionalImage)
