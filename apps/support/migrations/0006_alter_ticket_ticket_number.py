# Generated by Django 4.1 on 2022-09-28 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_alter_ticket_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_number',
            field=models.CharField(default='4606336780', editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
