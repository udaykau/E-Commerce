from django.db import models
import os
# Create your models here.


def get_upload_path(instance, filename):
    os.path.join('media/', instance.product_name)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    dire = '{0}/{1}'.format(instance.product_name, filename)
    return str(dire)


class Product(models.Model):
    sno = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=30)
    product_Description = models.CharField(max_length=1000)
    Large_Description = models.CharField(max_length=5000)
    Manufacturer = models.CharField(max_length=500)
    Gender = models.CharField(max_length=30,blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to=get_upload_path)
    image2 = models.ImageField(null=True, blank=True, upload_to=get_upload_path)
    image3 = models.ImageField(null=True, blank=True, upload_to=get_upload_path)
    image4 = models.ImageField(null=True, blank=True,upload_to=get_upload_path)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    sno = models.AutoField(primary_key=True)
    product_sno = models.CharField(max_length=20)
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    total_price = models.CharField(max_length=50)

    def __str__(self):
        return self.product_sno + ' ' + self.product_name
