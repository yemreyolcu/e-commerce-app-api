# Generated by Django 4.1.1 on 2022-10-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='post_image',
            field=models.ImageField(default='https://static.wixstatic.com/media/36f216_0d8f83a94504496faea07d9ca0fa5e7a~mv2.jpg/v1/fill/w_640,h_456,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/36f216_0d8f83a94504496faea07d9ca0fa5e7a~mv2.jpg', null=True, upload_to='images/'),
        ),
    ]
