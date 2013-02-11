from django.db import connections, transaction
from publications.models import Publication, Monthly
from django.core.exceptions import ObjectDoesNotExist


def run():
    cursor = connections['legacy'].cursor()
    cursor.execute(
        ("select data_status, date_stamp, publication_date_id "
         "from core_publication")
    )

    for row in cursor.fetchall():
        try:
            data_period = Monthly.objects.get(legacy_id=row[2])
            print data_period
        except ObjectDoesNotExist:
            print "missing"

        _, created = Publication.objects.get_or_create(
            date_stamp=row[1],
            defaults={'data_status': row[0],
                      'date_stamp': row[1],
                      'data_collection_period': data_period
                      }
        )

if __name__ == '__main__':
    run()
