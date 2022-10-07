from django.contrib import admin

from computer.models import Computer, CPU, Disk, Memory

# Register your models here.

admin.site.register(Computer)
admin.site.register(CPU)
admin.site.register(Disk)
admin.site.register(Memory)
