# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Publication.publication_date'
        db.delete_column(u'publications_publication', 'publication_date_id')

        # Adding field 'Publication.data_collection_period'
        db.add_column(u'publications_publication', 'data_collection_period',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['publications.Monthly'], unique=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Publication.publication_date'
        db.add_column(u'publications_publication', 'publication_date',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['publications.Monthly'], unique=True),
                      keep_default=False)

        # Deleting field 'Publication.data_collection_period'
        db.delete_column(u'publications_publication', 'data_collection_period_id')


    models = {
        u'publications.monthly': {
            'Meta': {'ordering': "['dateix']", 'object_name': 'Monthly'},
            'dateix': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'publications.publication': {
            'Meta': {'ordering': "['-data_collection_period']", 'object_name': 'Publication'},
            'data_collection_period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publications.Monthly']", 'unique': 'True'}),
            'data_status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'date_stamp': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['publications']