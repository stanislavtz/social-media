# Generated by Django 5.1.4 on 2024-12-18 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_profile_img_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='NoImage.png', null=True, upload_to='image/users'),
        ),
    ]
