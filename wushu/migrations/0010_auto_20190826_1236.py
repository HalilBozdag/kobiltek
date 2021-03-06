# Generated by Django 2.2.1 on 2019-08-26 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wushu', '0009_auto_20190826_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='communication',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wushu.City', verbose_name='İl'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='communication',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wushu.Country', verbose_name='Ülke'),
            preserve_default=False,
        ),
    ]
