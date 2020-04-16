from django.contrib import admin

from .models import Order, Comment, Note, CompletedWork, Payment

admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Note)
admin.site.register(CompletedWork)
admin.site.register(Payment)
