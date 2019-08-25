# Generated by Django 2.2.1 on 2019-08-24 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wushu', '0005_auto_20190824_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judge',
            name='punishment',
        ),
        migrations.RemoveField(
            model_name='judge',
            name='visa',
        ),
        migrations.AddField(
            model_name='judge',
            name='communication',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='wushu.Communication'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='judge',
            name='person',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='wushu.Person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='judge',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]