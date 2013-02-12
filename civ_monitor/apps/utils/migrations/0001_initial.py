# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Currency'
        db.create_table(u'utils_currency', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=4, primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('numcode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utils', ['Currency'])


    def backwards(self, orm):
        # Deleting model 'Currency'
        db.delete_table(u'utils_currency')


    models = {
        u'utils.currency': {
            'Meta': {'ordering': "('code',)", 'object_name': 'Currency'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['utils']