# Generated by Django 3.0.2 on 2020-02-01 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_auto_20200124_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_first_name', models.CharField(max_length=50)),
                ('customer_last_name', models.CharField(max_length=50)),
                ('customer_email', models.EmailField(max_length=50)),
                ('customer_phone', models.BigIntegerField()),
                ('customer_password', models.CharField(max_length=15)),
                ('customer_DOB', models.DateField()),
                ('customer_gender', models.CharField(max_length=6)),
                ('customer_address', models.CharField(max_length=250)),
            ],
        ),
    ]