# Generated by Django 4.2 on 2023-04-19 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackermanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assettype',
            name='assettype',
            field=models.CharField(max_length=50, unique=True, verbose_name='Asset Type'),
        ),
        migrations.AlterField(
            model_name='assettype',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='manageasset',
            name='assetimage',
            field=models.ImageField(default=None, upload_to='images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='manageasset',
            name='assetname',
            field=models.CharField(max_length=50, verbose_name='Asset Name'),
        ),
        migrations.AlterField(
            model_name='manageasset',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]