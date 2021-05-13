# Generated by Django 3.1.3 on 2020-12-28 09:15

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('product_sno', models.CharField(blank=True, max_length=20, null=True)),
                ('product_name', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('number', models.IntegerField(default=1)),
                ('total_price', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=30)),
                ('product_Description', models.CharField(max_length=1000)),
                ('Large_Description', models.CharField(max_length=5000)),
                ('Manufacturer', models.CharField(max_length=500)),
                ('Gender', models.CharField(blank=True, max_length=30)),
                ('image1', models.ImageField(blank=True, null=True, upload_to=products.models.get_upload_path)),
                ('image2', models.ImageField(blank=True, null=True, upload_to=products.models.get_upload_path)),
                ('image3', models.ImageField(blank=True, null=True, upload_to=products.models.get_upload_path)),
                ('image4', models.ImageField(blank=True, null=True, upload_to=products.models.get_upload_path)),
            ],
        ),
    ]