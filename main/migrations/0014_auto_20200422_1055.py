# Generated by Django 2.2.11 on 2020-04-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_pdftemplate_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdftemplate',
            name='pdf_text',
            field=models.TextField(verbose_name='Текст пдф'),
        ),
    ]
