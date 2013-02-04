from django.db import connection, transaction
from apps.publications.models import Publication


def run():
    cursor = connection.cursor()
    cursor.execute("select * from core_publication")
    for row in cursor.fetchall():
        print row
