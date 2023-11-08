from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    image = models.ImageField(upload_to='product/', verbose_name='превью', **NULLABLE)
    description = models.CharField(max_length=100, verbose_name='описание', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория', **NULLABLE)
    price = models.IntegerField(verbose_name='цена', **NULLABLE)

    def __str__(self):
        return f'{self.name} | описание: {self.description}\n {self.category}\n {self.price}'

    class Meta:
        ordering = ('name',)


