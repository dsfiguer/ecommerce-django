# Generated by Django 4.1 on 2022-10-05 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='KTQV4647', editable=False, max_length=8, primary_key=True, serialize=False, unique=True),
        ),
    ]
