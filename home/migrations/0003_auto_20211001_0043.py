# Generated by Django 3.2.7 on 2021-09-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211001_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spare_part',
            name='vehicle',
        ),
        migrations.AlterField(
            model_name='spare_part',
            name='brand',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='spare_part',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='spare_part',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
