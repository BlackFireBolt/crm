from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta


def now_plus_5():
    return datetime.now()+timedelta(days=5)


class Order(models.Model):
    # client------------------------------------------------------
    client_name = models.CharField(max_length=32, verbose_name='Имя клиента')
    phone = models.CharField(max_length=32, verbose_name='Телефон')

    OPTIONS = (
        ('n', 'Not set'),
        ('a', 'Acquaintances'),
        ('i', 'Internet'),
        ('O', 'Outdoor advertising'),
    )

    status = models.CharField(max_length=1, choices=OPTIONS, blank=True, default='n',
                              verbose_name='Откуда узнал о мастерской')

    # devices and malfunctions-------------------------------------
    device_type = models.CharField(max_length=32, blank=True, verbose_name='Тип устройства')
    serial_number = models.CharField(max_length=32, blank=True, verbose_name='Серийный номер/IMEI')
    brand = models.CharField(max_length=32, blank=True, verbose_name='Брэнд')
    model = models.CharField(max_length=32, blank=True, verbose_name='Модель')
    equipment = models.TextField(blank=True, verbose_name='Комплектация')
    appearance = models.CharField(default='Потертости, царапины', max_length=32, blank=True, verbose_name='Внешний вид')
    password = models.CharField(max_length=32, blank=True, verbose_name='Пароль')
    malfunction = models.TextField(blank=True, verbose_name='Неисправность')

    # additional Information-----------------------------------------
    receiver_notes = models.TextField(blank=True, verbose_name='Заметки приемщика')
    indicative_price = models.CharField(blank=True, max_length=32, verbose_name='Ориентировочная цена')
    quickly = models.BooleanField(default=False, verbose_name="Срочно")
    availability_date = models.DateTimeField(default=now_plus_5, blank=True, verbose_name="Срок заказа")
    receipt_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Поступил')

    # ----------------------------------------------------------------
    executor = models.CharField(max_length=32, blank=True, verbose_name='Исполнитель')
    prepayment = models.CharField(max_length=32, blank=True, verbose_name='Предоплата')
    # ----------------------------------------------------------------
    executor_note = models.TextField(blank=True, verbose_name="Комментарий исполнителя")
    verdict = models.TextField(blank=True, verbose_name="Вердикт / рекомендации клиенту")
    # ----------------------------------------------------------------
    done = models.BooleanField(default=False, verbose_name="Готово")
    # ----------------------------------------------------------------

    def get_absolute_url(self):
        return reverse("main:order-detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-receipt_date']


class Comment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    comment = models.TextField(verbose_name="Комментарий")

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Task(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    task = models.TextField(verbose_name="Задача")

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Note(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    text = models.TextField(verbose_name="Заметка")

    OPTIONS = (
        ('c', 'Comment'),
        ('t', 'Task'),
    )
    note_type = models.CharField(max_length=1, choices=OPTIONS, default='c', verbose_name='Тип заметки')

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"


class CompletedWork(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    work = models.TextField(verbose_name="Работа")
    amount = models.DecimalField(default=1, max_digits=5, decimal_places=2, verbose_name="Количество")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")
    cost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Стоимость")
    warranty = models.DecimalField(default=30, max_digits=4, decimal_places=0, verbose_name='Гарантия')

    class Meta:
        verbose_name = "Выполненная работа"
        verbose_name_plural = "Выполненные работы"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    description = models.TextField(verbose_name="Работа")
    data = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')
    total = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Сумма")
    OPTIONS = (
        ('c', 'Расход'),
        ('i', 'Приход'),
    )
    type = models.CharField(max_length=1, choices=OPTIONS, default='c', verbose_name='Тип платежа')

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"


class Income(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    description = models.TextField(verbose_name="Работа")
    data = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')
    total = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Сумма")


class Consumption(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    description = models.TextField(verbose_name="Работа")
    data = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')
    total = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Сумма")
