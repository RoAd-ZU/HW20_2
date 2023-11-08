from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        products_list = [
            {'name':'змея', 'image': 'media/Snake.jpg', 'description':'ужужужужуж', 'category':'от ежа', 'price':100},
            {'name':'чупачупс', 'image':'media/Chupa.jpg', 'description':'погрызен, упакован', 'category':'набор педофила', 'price':45},
            {'name':'плавки-невидимки', 'image':'media/Hmm.jpg', 'description':'свобода движений и ветер щекочет', 'category':'шнурки пляжные', 'price':12000},
            {'name':'молоток подвесной (чугунный)', 'image':'media/Hummer.jpg', 'description':'доп.комплектация к будильнику "Один раз живём"', 'category':'доброе утро', 'price':2100}
        ]

        products_cr = []
        for item in products_list:
            products_cr.append(Product(**item))

        Product.objects.bulk_create(products_cr)