# Generated by Django 4.1.1 on 2022-10-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(max_length=555, null=True),
        ),
    ]
