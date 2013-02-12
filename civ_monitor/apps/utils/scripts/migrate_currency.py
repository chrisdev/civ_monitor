from utils.models import Currency
from django.db import connections, transaction
from django.core.exceptions import ObjectDoesNotExist


def run():

    cursor = connections['legacy'].cursor()
    cursor.execute(
        (
            "select code, description, numcode from core_currency"

        )
    )
    for row in cursor.fetchall():

        obj, created = Currency.objects.get_or_create(
            code=row[0],
            defaults={'description': row[1],
                       'numcode' : row[2]
                     }
        )
