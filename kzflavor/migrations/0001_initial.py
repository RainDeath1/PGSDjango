# Generated by Django 4.2.2 on 2023-09-27 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import kzflavor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin', kzflavor.models.KZIINField(max_length=12, verbose_name='ИИН')),
                ('id_card', kzflavor.models.KZIDCardField(max_length=9, verbose_name='Номер удостоверения')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]