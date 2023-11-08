# Generated by Django 4.2.7 on 2023-11-08 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='категория'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='цена'),
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]