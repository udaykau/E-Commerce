# Generated by Django 3.1.5 on 2021-01-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_sno',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.CharField(max_length=50),
        ),
    ]
