# Generated by Django 2.2.4 on 2019-08-29 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0003_auto_20190528_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='objective',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='indicators.Objective'),
        ),
    ]
