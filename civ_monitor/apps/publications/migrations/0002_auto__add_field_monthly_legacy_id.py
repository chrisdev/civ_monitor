# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Monthly.legacy_id'
        db.add_column(u'publications_monthly', 'legacy_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Monthly.legacy_id'
        db.delete_column(u'publications_monthly', 'legacy_id')


    models = {
        u'publications.monthly': {
            'Meta': {'ordering': "['dateix']", 'object_name': 'Monthly'},
            'dateix': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'publications.publication': {
            'Meta': {'ordering': "['-publication_date']", 'object_name': 'Publication'},
            'data_status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'date_stamp': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publications.Monthly']", 'unique': 'True'})
        }
    }

    complete_apps = ['publications']