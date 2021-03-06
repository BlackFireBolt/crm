# Generated by Django 2.2.11 on 2020-03-22 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200213_1306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='completedwork',
            options={'verbose_name': 'Выполненная работа', 'verbose_name_plural': 'Выполненные работы'},
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Работа')),
                ('data', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')),
                ('total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Сумма')),
                ('type', models.CharField(choices=[('c', 'Расход'), ('i', 'Приход')], default='c', max_length=1, verbose_name='Тип платежа')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Order', verbose_name='Заказ')),
            ],
        ),
    ]
