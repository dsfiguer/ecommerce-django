# Generated by Django 4.1 on 2022-10-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0006_alter_ticket_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_number',
            field=models.CharField(default='2924287064', editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]