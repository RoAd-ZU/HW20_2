import psycopg2
from django.core.management import BaseCommand

from catalog.models import Product, Description


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        conn = psycopg2.connect(host='localhost', database='hw20_2_', user='postgres')
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('TRUNCATE TABLE catalog_product RESTART IDENTITY CASCADE')


        finally:
            conn.close()
        Product.objects.all()
        products_list = [
            {'name': 'змея', 'image': ''},
            {'name': 'чупачупс', 'image': ''},
            {'name': 'плавки-невидимки', 'image': ''},
            {'name': 'молоток подвесной (чугунный)', 'image': ''}
        ]

        products_cr = []
        for item in products_list:
            products_cr.append(Product(**item))

        Product.objects.bulk_create(products_cr)

        Description.objects.all().delete()
        conn = psycopg2.connect(host='localhost', database='hw20_2_', user='postgres')
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('TRUNCATE TABLE catalog_description RESTART IDENTITY')

        finally:
            conn.close()
        products_list = [
            {'name_id': 1, 'description': 'ужужужужуж', 'category': 'от ежа', 'price': 100},
            {'name_id': 2, 'description': 'погрызен, упакован', 'category': 'набор педофила', 'price': 45},
            {'name_id': 3, 'description': 'свобода движений и ветер щекочет',
             'category': 'шнурки пляжные', 'price': 12000},
            {'name_id': 4, 'description': 'доп.комплектация к будильнику "Один раз живём"',
             'category': 'доброе утро', 'price': 2100}
        ]

        products_cr = []
        for item in products_list:
            products_cr.append(Description(**item))

        Description.objects.bulk_create(products_cr)
