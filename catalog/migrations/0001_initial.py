# Generated by Django 4.2.7 on 2023-11-06 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='превью')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='описание')),
                ('category', models.CharField(max_length=100, verbose_name='категория')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='наименование')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]