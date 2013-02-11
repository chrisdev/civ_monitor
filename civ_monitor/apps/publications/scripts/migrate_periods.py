from django.db import connections, transaction
from publications.models import Monthly


def run():
    cursor = connections['legacy'].cursor()
    cursor.execute(
        (
            "select id, dateix from freqdates_monthly "
            "where extract(year from dateix) >= 2006  "
            "and extract(year from dateix) < 2013"
            "order by dateix"
        )
    )
    for row in cursor.fetchall():
        print row

        obj, created = Monthly.objects.get_or_create(
            dateix=row[1],
            defaults={'legacy_id': row[0]}
        )

        if created:
            print obj
