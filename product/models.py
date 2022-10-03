from django.db import models
from computer.models import Computer, CPU, Disk, Memory
from default.models import OS, Brand
# Create your models here.


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    os = models.ForeignKey(OS, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    disk = models.ForeignKey(Disk, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    price = models.FloatField(default=0)
    website = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.brand.name