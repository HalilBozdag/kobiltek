# Generated by Django 2.2.1 on 2019-08-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wushu', '0004_auto_20190822_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='beltFinishDate',
            field=models.DateField(null=True, verbose_name='Kuşak Bitiş Tarihi'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='beltStartDate',
            field=models.DateField(null=True, verbose_name='Kuşak Başlama Tarihi'),
        ),
    ]
