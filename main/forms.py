from django import forms
from tempus_dominus.widgets import DateTimePicker


from .models import Order, Comment, Note, CompletedWork, Payment


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['client_name', 'phone', 'quickly', 'availability_date', 'device_type', 'serial_number', 'brand', 'model',
                  'equipment', 'appearance', 'password', 'malfunction', 'receiver_notes', 'indicative_price', 'executor', 'prepayment',
                  'executor_note', 'verdict', ]
        widgets = {
            'client_name': forms.TextInput(attrs={
                'id': 'post-client_name',
                'class': 'form-control', 
                'required': True, 
            }),
            'phone': forms.TextInput(attrs={
                'id': 'post-phone', 
                'class': 'form-control', 
                'required': True, 
            }),
            'quickly': forms.CheckboxInput(attrs={
                'id': 'post-quickly',
                'class': 'form-check-input',
                'required': False
            }),
            'availability_date': forms.DateTimeInput(attrs={
                'id': 'post-availability_date',
                'class': 'form-control',
            }),
            'device_type': forms.TextInput(attrs={
                'id': 'post-device_type',
                'class': 'form-control', 
            }),
            'serial_number': forms.TextInput(attrs={
                'id': 'post-serial_number',
                'class': 'form-control', 
            }),
            'brand': forms.TextInput(attrs={
                'id': 'post-brand',
                'class': 'form-control',  
            }),
            'model': forms.TextInput(attrs={
                'id': 'post-model',
                'class': 'form-control', 
            }),
            'equipment': forms.Textarea(attrs={
                'id': 'post-equipment',
                'class': 'form-control',
            }),
            'appearance': forms.TextInput(attrs={
                'id': 'post-appearance',
                'class': 'form-control',
            }),
            'password': forms.TextInput(attrs={
                'id': 'post-password',
                'class': 'form-control', 
            }),
            'malfunction': forms.Textarea(attrs={
                'id': 'post-malfunction',
                'class': 'form-control',
            }),
            'receiver_notes': forms.Textarea(attrs={
                'id': 'post-receiver_notes',
                'class': 'form-control',
            }),
            'indicative_price': forms.TextInput(attrs={
                'id': 'post-indicative_price',
                'class': 'form-control', 
            }),
            'executor': forms.TextInput(attrs={
                'id': 'post-executor',
                'class': 'form-control', 
            }),
            'prepayment': forms.TextInput(attrs={
                'id': 'post-prepayment',
                'class': 'form-control', 
            }),
            'executor_note': forms.Textarea(attrs={
                'id': 'post-executor_note',
                'class': 'form-control',
            }),
            'verdict': forms.Textarea(attrs={
                'id': 'post-verdict',
                'class': 'form-control',
            }),
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text', ]
        widgets = {
            'text': forms.Textarea(attrs={
                'id': 'postText',
                'class': 'form-control',
                'required': True,
                'placeholder': 'Добавить'
            }),
        }


class CompletedWorkForm(forms.ModelForm):
    class Meta:
        model = CompletedWork
        fields = ['work', 'amount', 'price', 'warranty', ]
        widgets = {
            'work': forms.Textarea(attrs={
                'id': 'post-work',
                'class': 'form-control',
                'required': True
            }),
            'amount': forms.NumberInput(attrs={
                'id': 'post-amount',
                'required': True
            }),
            'price': forms.NumberInput(attrs={
                'id': 'post-price',
                'required': True
            }),
            'warranty': forms.NumberInput(attrs={
                'id': 'post-warranty',
                'required': True
            }),
        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['description', 'total', ]
        widgets = {
            'description': forms.Textarea(attrs={
                'id': 'post-income-description',
                'class': 'form-control',
                'required': True
            }),
            'total': forms.NumberInput(attrs={
                'id': 'post-income-total',
                'required': True,
            }),
        }


class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['description', 'total', ]
        widgets = {
            'description': forms.Textarea(attrs={
                'id': 'post-consumption-description',
                'class': 'form-control',
                'required': True
            }),
            'total': forms.NumberInput(attrs={
                'id': 'post-consumption-total',
                'required': True,
            }),
        }

