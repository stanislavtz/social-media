# Generated by Django 5.1.4 on 2024-12-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='NoImage.png', null=True, upload_to='users'),
        ),
    ]