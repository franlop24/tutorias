# Generated by Django 5.0.6 on 2024-07-03 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.category', verbose_name='Categoría'),
        ),
    ]
