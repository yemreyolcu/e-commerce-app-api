from django.db import models


# Create your models here.

class Computer(models.Model):
    model_number = models.CharField(max_length=100)  # model of computer
    serial_number = models.CharField(max_length=100)

    def __str__(self):
        return self.model_number


class CPU(models.Model):
    cpu_type = models.CharField(max_length=100)  # model of cpu
    cpu_generation = models.CharField(max_length=100)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)

    def __str__(self):
        return self.cpu_type + " " + self.cpu_generation


class Disk(models.Model):
    disk_type = models.CharField(max_length=100)  # model of disk
    disk_size = models.CharField(max_length=100)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)

    def __str__(self):
        return self.disk_type + " " + self.disk_size


class Memory(models.Model):
    memory_size = models.CharField(max_length=100)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)

    def __str__(self):
        return self.memory_type + " " + self.memory_size