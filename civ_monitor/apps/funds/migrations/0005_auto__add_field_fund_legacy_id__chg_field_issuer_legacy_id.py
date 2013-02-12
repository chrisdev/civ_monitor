# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Fund.legacy_id'
        db.add_column(u'funds_fund', 'legacy_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


        # Changing field 'Issuer.legacy_id'
        db.alter_column(u'funds_issuer', 'legacy_id', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Fund.legacy_id'
        db.delete_column(u'funds_fund', 'legacy_id')


        # Changing field 'Issuer.legacy_id'
        db.alter_column(u'funds_issuer', 'legacy_id', self.gf('django.db.models.fields.IntegerField')(default=2))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'funds.activestatus': {
            'Meta': {'object_name': 'ActiveStatus'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'fund': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activity_status'", 'to': "orm['funds.Fund']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'update_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'funds.fund': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Fund'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['utils.Currency']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fund_classification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.InternationalClassification']"}),
            'fund_scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.FundScheme']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'funds'", 'to': "orm['funds.Issuer']"}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'legal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.LegalStatus']"}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'open_ended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'registration_date': ('django.db.models.fields.DateField', [], {}),
            'symbol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        },
        'funds.fundscheme': {
            'Meta': {'object_name': 'FundScheme'},
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funds.internationalclassification': {
            'Meta': {'object_name': 'InternationalClassification'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'fund_type': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'funds.issuer': {
            'Meta': {'ordering': "('name', 'symbol')", 'object_name': 'Issuer'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_local_entity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'funds.legalstatus': {
            'Meta': {'object_name': 'LegalStatus'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'utils.currency': {
            'Meta': {'ordering': "('code',)", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['funds']