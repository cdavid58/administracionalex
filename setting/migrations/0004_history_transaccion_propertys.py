# Generated by Django 3.2.8 on 2023-03-17 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
        ('setting', '0003_movement_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history_transaccion',
            name='propertys',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.property'),
        ),
    ]