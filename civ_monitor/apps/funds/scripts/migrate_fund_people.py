from funds.models import (
    Fund, Issuer,
    OfficerDirector, ServiceManager,
    FundServiceManager, FundOfficer, IssuerOfficer
)

from django.db import connections
from django.core.exceptions import ObjectDoesNotExist

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def run():

    cursor = connections['legacy'].cursor()
    cursor.execute(
        (
            "select id, name, address_1, address_2, telephone, fax,  "
            "country_id, website "
            "from core_servicemanager"
        )
    )
    print "Service Manager"
    for row in cursor.fetchall():
        _, created = ServiceManager.objects.get_or_create(
            name=row[1],
            defaults={
                'address_1': row[2],
                'address_2': row[3],
                'telephone': row[4],
                'fax': row[5],
                'country': row[6],
                'website': row[7],
                'legacy_id': row[0]
            }
        )

    print "Officer Director"
    cursor.execute(
        (
            "select id, first_name, last_name, telephone, fax, email, "
            "address_1, address_2, country_id "
            "from core_officerdirector"
        )
    )

    for row in cursor.fetchall():
        _, created = OfficerDirector.objects.get_or_create(
            legacy_id=row[0],
            defaults={
                'first_name': row[1],
                'last_name': row[2],
                'telephone': row[3],
                'fax': row[4],
                'email': row[5],
                'address_1': row[6],
                'address_2': row[7],
                'country': row[8],
            }

        )
    print "FundServiceManager"
    cursor.execute(
        (
            "select f.symbol, fsm.company_id, p.description, fsm.active "
            "from core_fundservicemanager fsm, core_servicemanager sm, core_fund f, core_position p "
            "where fsm.fund_id=f.id and fsm.company_id=sm.id and fsm.position_id=p.id"
        )
    )

    for row in cursor.fetchall():
        sm = ServiceManager.objects.get(legacy_id=row[1])
        fund = Fund.objects.get(symbol=row[0])

        _, created = FundServiceManager.objects.get_or_create(
            fund=fund,
            service_manager=sm,
            defaults={
                'position': row[2],
            }
        )

    print "FundOfficer"
    cursor.execute(
        (
           "select f.symbol, fo.officer_id, p.description "
           "from core_fundofficer fo, core_fund f, core_position p "
           "where fo.fund_id=f.id and fo.position_id=p.id"
        )
    )
    for row in cursor.fetchall():
       # print row
        try:
            fund = Fund.objects.get(symbol=row[0])
        except ObjectDoesNotExist:
            print "Fund {} missing".format(row[0])

        o = OfficerDirector.objects.get(legacy_id=row[1])

        _, created = FundOfficer.objects.get_or_create(
            fund=fund,
            officer=o,
            defaults={
                'position': row[2],
            }
        )

    print "IssuerOfficer"
    cursor.execute(
        (
           "select i.symbol, io.officer_id, p.description "
           "from core_issuerofficer io, core_issuer i, core_position p "
           "where io.issuer_id=i.id and io.position_id=p.id"
        )

    )
    for row in cursor.fetchall():
        issuer = Issuer.objects.get(symbol=row[0])
        o = OfficerDirector.objects.get(legacy_id=row[1])

        _, created = IssuerOfficer.objects.get_or_create(
            issuer=fund,
            officer=o,
            defaults={
                'position': row[2],
            }
        )

