from django.contrib import admin

from computer.models import Computer, CPU, Disk, Memory


# Register your models here.

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('model_number', 'serial_number')


@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    list_display = ('cpu_type', 'cpu_generation', 'computer')


@admin.register(Disk)
class DiskAdmin(admin.ModelAdmin):
    list_display = ('disk_type', 'disk_size', 'computer')


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('memory_size', 'computer')
