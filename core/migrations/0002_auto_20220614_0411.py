# Generated by Django 3.2.13 on 2022-06-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='codigo',
        ),
        migrations.AlterField(
            model_name='produto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
