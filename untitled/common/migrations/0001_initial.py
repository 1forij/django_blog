# Generated by Django 2.2.5 on 2022-06-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phoneNumber', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=60)),
            ],
        ),
    ]
