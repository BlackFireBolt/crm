# Generated by Django 2.2.11 on 2020-04-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200420_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdftemplate',
            name='name',
            field=models.CharField(default='temp', max_length=32, verbose_name='Имя'),
            preserve_default=False,
        ),
    ]
