# Generated by Django 4.1 on 2022-10-03 01:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('url', models.URLField()),
                ('logo', models.ImageField(upload_to='site/logo/')),
                ('favicon', models.ImageField(upload_to='site/favicon/')),
                ('created_at', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('is_available', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
