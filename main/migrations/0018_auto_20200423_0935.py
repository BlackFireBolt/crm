# Generated by Django 2.2.11 on 2020-04-23 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20200423_0933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-date'], 'verbose_name': 'Платеж', 'verbose_name_plural': 'Платежи'},
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='data',
            new_name='date',
        ),
    ]
