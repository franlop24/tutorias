# Generated by Django 5.0.6 on 2024-07-18 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocational', '0004_remove_exam_career_remove_exam_stage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stage',
        ),
    ]
