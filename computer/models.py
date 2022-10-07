from django.db import models

from default.models import Brand, OS


# Create your models here.

class CPU(models.Model):
    cpu_type = models.CharField(max_length=100)  # model of cpu
    cpu_generation = models.CharField(max_length=100)

    def __str__(self):
        return self.cpu_type + " " + self.cpu_generation


class Disk(models.Model):
    disk_type = models.CharField(max_length=100)  # model of disk
    disk_size = models.CharField(max_length=100)

    def __str__(self):
        return self.disk_type + " " + self.disk_size


class Memory(models.Model):
    memory_size = models.CharField(max_length=100)

    def __str__(self):
        return self.memory_size


class Computer(models.Model):
    model_number = models.CharField(max_length=100)  # model of computer
    serial_number = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, related_name='computer_cpu')
    disk = models.ForeignKey(Disk, on_delete=models.CASCADE, related_name='computer_disk')
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, related_name='computer_memory')
    os = models.ForeignKey(OS, on_delete=models.CASCADE, related_name='computer_os')

    def __str__(self):
        return self.model_number
