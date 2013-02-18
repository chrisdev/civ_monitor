# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ServiceManager'
        db.create_table('funds_servicemanager', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('funds', ['ServiceManager'])

        # Adding model 'FundServiceManager'
        db.create_table('funds_fundservicemanager', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fund', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funds.Fund'])),
            ('service_manager', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funds.ServiceManager'])),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('funds', ['FundServiceManager'])

        # Adding model 'Position'
        db.create_table('funds_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('funds', ['Position'])

        # Adding model 'IssuerOfficer'
        db.create_table('funds_issuerofficer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issuer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='issuer_officers', to=orm['funds.Issuer'])),
            ('officer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funds.OfficerDirector'])),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funds.Position'])),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('funds', ['IssuerOfficer'])

        # Adding unique constraint on 'IssuerOfficer', fields ['officer', 'issuer']
        db.create_unique('funds_issuerofficer', ['officer_id', 'issuer_id'])

        # Adding model 'OfficerDirector'
        db.create_table('funds_officerdirector', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100, null=True, blank=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2, blank=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'], null=True, blank=True)),
        ))
        db.send_create_signal('funds', ['OfficerDirector'])

        # Adding model 'FundOfficer'
        db.create_table('funds_fundofficer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fund', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fund_officers', to=orm['funds.Fund'])),
            ('officer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funds.OfficerDirector'])),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funds.Position'])),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('funds', ['FundOfficer'])


    def backwards(self, orm):
        # Removing unique constraint on 'IssuerOfficer', fields ['officer', 'issuer']
        db.delete_unique('funds_issuerofficer', ['officer_id', 'issuer_id'])

        # Deleting model 'ServiceManager'
        db.delete_table('funds_servicemanager')

        # Deleting model 'FundServiceManager'
        db.delete_table('funds_fundservicemanager')

        # Deleting model 'Position'
        db.delete_table('funds_position')

        # Deleting model 'IssuerOfficer'
        db.delete_table('funds_issuerofficer')

        # Deleting model 'OfficerDirector'
        db.delete_table('funds_officerdirector')

        # Deleting model 'FundOfficer'
        db.delete_table('funds_fundofficer')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': "orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['filer.File']},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'funds.activestatus': {
            'Meta': {'object_name': 'ActiveStatus'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'fund': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activity_status'", 'to': "orm['funds.Fund']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'funds.fund': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Fund'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['utils.Currency']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fund_classification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.InternationalClassification']"}),
            'fund_scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.FundScheme']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'funds'", 'to': "orm['funds.Issuer']"}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'legal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.LegalStatus']"}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'open_ended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'registration_date': ('django.db.models.fields.DateField', [], {}),
            'symbol': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'})
        },
        'funds.fundofficer': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'FundOfficer'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fund': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fund_officers'", 'to': "orm['funds.Fund']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'officer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.OfficerDirector']"}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.Position']"})
        },
        'funds.fundscheme': {
            'Meta': {'object_name': 'FundScheme'},
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funds.fundservicemanager': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'FundServiceManager'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fund': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.Fund']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service_manager': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.ServiceManager']"})
        },
        'funds.internationalclassification': {
            'Meta': {'object_name': 'InternationalClassification'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'fund_type': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_local_entity': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'funds.issuerofficer': {
            'Meta': {'ordering': "('_order',)", 'unique_together': "(('officer', 'issuer'),)", 'object_name': 'IssuerOfficer'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issuer_officers'", 'to': "orm['funds.Issuer']"}),
            'officer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.OfficerDirector']"}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.Position']"})
        },
        'funds.legalstatus': {
            'Meta': {'object_name': 'LegalStatus'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funds.officerdirector': {
            'Meta': {'ordering': "('last_name', 'first_name')", 'object_name': 'OfficerDirector'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'})
        },
        'funds.position': {
            'Meta': {'ordering': "('description',)", 'object_name': 'Position'},
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funds.servicemanager': {
            'Meta': {'ordering': "('name', 'country')", 'object_name': 'ServiceManager'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'utils.currency': {
            'Meta': {'ordering': "('code',)", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['funds']