# Generated by Django 4.2.2 on 2023-06-21 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due_data',
            new_name='due_date',
        ),
    ]
