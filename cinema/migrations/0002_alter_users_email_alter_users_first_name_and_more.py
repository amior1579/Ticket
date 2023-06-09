# Generated by Django 4.1.7 on 2023-04-19 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=250),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
