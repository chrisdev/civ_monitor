
from funds.models import (InternationalClassification, LegalStatus, FundScheme,
                          Issuer, Fund)
from utils.models import Currency

from django.db import connections


def run():

    cursor = connections['legacy'].cursor()
    cursor.execute(
        (
            "select code, description, fund_type, name "
            "from core_fundclassification"
        )
    )
    print "Fund Classification"
    for row in cursor.fetchall():
        _, created = InternationalClassification.objects.get_or_create(
            code=row[0],
            defaults={'description': row[1],
                      'fund_type': row[2],
                      'name': row[3]
                      }
        )

    print "Legal"
    cursor.execute("select id, description from core_fundlegal")

    for row in cursor.fetchall():
        _, created = LegalStatus.objects.get_or_create(
            code=str(row[0]),
            defaults={'description': row[1]}
        )
    print "Scheme"
    cursor.execute("select id, description from core_fundscheme")
    for row in cursor.fetchall():

        _, created = FundScheme.objects.get_or_create(
            code=row[0],
            defaults={'description': row[1]}
        )

    print "Issuer"

    cursor.execute(
        (
            "select symbol, name, website, email, address_1, "
            "address_2, fax, telephone, country_id, is_local_entity, id "
            "from core_issuer"
        )
    )

    for row in cursor.fetchall():
        _, created = Issuer.objects.get_or_create(
            symbol=row[0],
            defaults={'name': row[1],
                      'website': row[2],
                      'email': row[3],
                      'address_1': 'NA' if row[4] is None else row[4],
                      'address_2': 'NA' if row[5] is None else row[5],
                      'fax': 'NA' if row[6] is None else row[6],
                      'telephone': 'NA' if row[7] is None else row[7],
                      'country': row[8],
                      'is_local_entity': row[9],
                      'legacy_id': row[10]
                      }

        )

    print "FUND"
    cursor.execute(
        (
            "select i.symbol, f.symbol, f.description, f.country_id,"
            "f.currency_id, f.fund_classification_id, fund_scheme_id, "
            "legal_id, open_ended, notes, registration_date, f.id "
            "from core_fund f, core_issuer i, core_fundclassification cl "
            "where f.issuer_id = i.id "
        )
    )
    for row in cursor.fetchall():

        i = Issuer.objects.get(symbol=row[0])
        currency = Currency.objects.get(code=row[4])
        fund_class = InternationalClassification.objects.get(code=row[5])
        fund_scheme = FundScheme.objects.get(code=row[6])
        legal_status = LegalStatus.objects.get(code=str(row[7]))
        try:
            _, created = Fund.objects.get_or_create(
                symbol=row[1],
                defaults={'issuer': i,
                          'description': row[2],
                          'country': 'LU' if len(row[3]) > 2 else row[3],
                          'currency': currency,
                          'fund_scheme': fund_scheme,
                          'fund_classification': fund_class,
                          'legal': legal_status,
                          'open_ended': row[8],
                          'notes': row[9],
                          'registration_date': row[10],
                          'legacy_id': row[11]
                          }
            )
        except:
            print "Bad Row "
            print row
