# Generated by Django 3.2.5 on 2021-09-08 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0028_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='account'),
        ),
        migrations.AddField(
            model_name='donation',
            name='isApproved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='donation',
            name='originalPrice',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='yearPurchased',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='testing'),
        ),
    ]
