# Generated by Django 2.0.1 on 2018-01-24 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('date', models.DateField(verbose_name='Date')),
                ('A_value', models.FloatField(verbose_name='A Value')),
                ('B_value', models.FloatField(verbose_name='B Value')),
            ],
        ),
    ]
