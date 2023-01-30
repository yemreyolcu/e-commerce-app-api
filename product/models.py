from django.db import models
from computer.models import Computer, CPU, Disk, Memory
from default.models import OS, Brand


# Create your models here.

class Product(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    price = models.FloatField(default=0)
    website = models.CharField(max_length=555, default="")
    url = models.CharField(max_length=555, null=True)
    image = models.TextField(default="", null=True)
    post_image = models.ImageField(upload_to='images/', default="/images/default-image2.jpg", null=True, max_length=355)

    # updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.computer.brand.name
