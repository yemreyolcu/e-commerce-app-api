from django.db import models
from computer.models import Computer, CPU, Disk, Memory
from default.models import OS, Brand

# Create your models here.

default_image = "https://static.wixstatic.com/media/36f216_0d8f83a94504496faea07d9ca0fa5e7a~mv2.jpg/v1/fill/w_640,h_456,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/36f216_0d8f83a94504496faea07d9ca0fa5e7a~mv2.jpg"


class Product(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    price = models.FloatField(default=0)
    website = models.CharField(max_length=100, default="")
    url = models.CharField(max_length=555, default="")
    image = models.TextField(default="", null=True)
    post_image = models.ImageField(upload_to='images/', default=default_image, null=True)

    def __str__(self):
        return self.computer.brand.name
