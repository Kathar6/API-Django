# Generated by Django 3.0.6 on 2020-05-21 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0010_auto_20200520_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.ComponentCategory'),
        ),
    ]
