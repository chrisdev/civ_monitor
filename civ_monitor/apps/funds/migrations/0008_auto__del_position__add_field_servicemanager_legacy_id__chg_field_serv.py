# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Position'
        db.delete_table('funds_position')

        # Adding field 'ServiceManager.legacy_id'
        db.add_column('funds_servicemanager', 'legacy_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


        # Changing field 'ServiceManager.website'
        db.alter_column('funds_servicemanager', 'website', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'ServiceManager.fax'
        db.alter_column('funds_servicemanager', 'fax', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'ServiceManager.telephone'
        db.alter_column('funds_servicemanager', 'telephone', self.gf('django.db.models.fields.CharField')(default='', max_length=50))
        # Adding field 'FundServiceManager.position'
        db.add_column('funds_fundservicemanager', 'position',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'FundServiceManager.effective_date'
        db.add_column('funds_fundservicemanager', 'effective_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FundServiceManager.status'
        db.add_column('funds_fundservicemanager', 'status',
                      self.gf('model_utils.fields.StatusField')(default='active', max_length=100, no_check_for_status=True),
                      keep_default=False)

        # Adding field 'FundServiceManager.notes'
        db.add_column('funds_fundservicemanager', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'FundServiceManager.updated_by'
        db.add_column('funds_fundservicemanager', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'IssuerOfficer.effective_date'
        db.add_column('funds_issuerofficer', 'effective_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'IssuerOfficer.status'
        db.add_column('funds_issuerofficer', 'status',
                      self.gf('model_utils.fields.StatusField')(default='active', max_length=100, no_check_for_status=True),
                      keep_default=False)

        # Adding field 'IssuerOfficer.notes'
        db.add_column('funds_issuerofficer', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'IssuerOfficer.updated_by'
        db.add_column('funds_issuerofficer', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)


        # Renaming column for 'IssuerOfficer.position' to match new field type.
        db.rename_column('funds_issuerofficer', 'position_id', 'position')
        # Changing field 'IssuerOfficer.position'
        db.alter_column('funds_issuerofficer', 'position', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Removing index on 'IssuerOfficer', fields ['position']
        db.delete_index('funds_issuerofficer', ['position_id'])

        # Adding field 'OfficerDirector.legacy_id'
        db.add_column('funds_officerdirector', 'legacy_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


        # Changing field 'OfficerDirector.fax'
        db.alter_column('funds_officerdirector', 'fax', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'OfficerDirector.telephone'
        db.alter_column('funds_officerdirector', 'telephone', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'OfficerDirector.email'
        db.alter_column('funds_officerdirector', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=50))
        # Adding field 'FundOfficer.effective_date'
        db.add_column('funds_fundofficer', 'effective_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FundOfficer.status'
        db.add_column('funds_fundofficer', 'status',
                      self.gf('model_utils.fields.StatusField')(default='active', max_length=100, no_check_for_status=True),
                      keep_default=False)

        # Adding field 'FundOfficer.notes'
        db.add_column('funds_fundofficer', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'FundOfficer.updated_by'
        db.add_column('funds_fundofficer', 'updated_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)


        # Renaming column for 'FundOfficer.position' to match new field type.
        db.rename_column('funds_fundofficer', 'position_id', 'position')
        # Changing field 'FundOfficer.position'
        db.alter_column('funds_fundofficer', 'position', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Removing index on 'FundOfficer', fields ['position']
        db.delete_index('funds_fundofficer', ['position_id'])


    def backwards(self, orm):
        # Adding index on 'FundOfficer', fields ['position']
        db.create_index('funds_fundofficer', ['position_id'])

        # Adding index on 'IssuerOfficer', fields ['position']
        db.create_index('funds_issuerofficer', ['position_id'])

        # Adding model 'Position'
        db.create_table('funds_position', (
            ('code', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('funds', ['Position'])

        # Deleting field 'ServiceManager.legacy_id'
        db.delete_column('funds_servicemanager', 'legacy_id')


        # Changing field 'ServiceManager.website'
        db.alter_column('funds_servicemanager', 'website', self.gf('django.db.models.fields.URLField')(max_length=100, null=True))

        # Changing field 'ServiceManager.fax'
        db.alter_column('funds_servicemanager', 'fax', self.gf('django.db.models.fields.CharField')(max_length=13, null=True))

        # Changing field 'ServiceManager.telephone'
        db.alter_column('funds_servicemanager', 'telephone', self.gf('django.db.models.fields.CharField')(max_length=13, null=True))
        # Deleting field 'FundServiceManager.position'
        db.delete_column('funds_fundservicemanager', 'position')

        # Deleting field 'FundServiceManager.effective_date'
        db.delete_column('funds_fundservicemanager', 'effective_date')

        # Deleting field 'FundServiceManager.status'
        db.delete_column('funds_fundservicemanager', 'status')

        # Deleting field 'FundServiceManager.notes'
        db.delete_column('funds_fundservicemanager', 'notes')

        # Deleting field 'FundServiceManager.updated_by'
        db.delete_column('funds_fundservicemanager', 'updated_by_id')

        # Deleting field 'IssuerOfficer.effective_date'
        db.delete_column('funds_issuerofficer', 'effective_date')

        # Deleting field 'IssuerOfficer.status'
        db.delete_column('funds_issuerofficer', 'status')

        # Deleting field 'IssuerOfficer.notes'
        db.delete_column('funds_issuerofficer', 'notes')

        # Deleting field 'IssuerOfficer.updated_by'
        db.delete_column('funds_issuerofficer', 'updated_by_id')


        # Renaming column for 'IssuerOfficer.position' to match new field type.
        db.rename_column('funds_issuerofficer', 'position', 'position_id')
        # Changing field 'IssuerOfficer.position'
        db.alter_column('funds_issuerofficer', 'position_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funds.Position']))
        # Deleting field 'OfficerDirector.legacy_id'
        db.delete_column('funds_officerdirector', 'legacy_id')


        # Changing field 'OfficerDirector.fax'
        db.alter_column('funds_officerdirector', 'fax', self.gf('django.db.models.fields.CharField')(max_length=13, null=True))

        # Changing field 'OfficerDirector.telephone'
        db.alter_column('funds_officerdirector', 'telephone', self.gf('django.db.models.fields.CharField')(max_length=13, null=True))

        # Changing field 'OfficerDirector.email'
        db.alter_column('funds_officerdirector', 'email', self.gf('django.db.models.fields.EmailField')(max_length=100, null=True))
        # Deleting field 'FundOfficer.effective_date'
        db.delete_column('funds_fundofficer', 'effective_date')

        # Deleting field 'FundOfficer.status'
        db.delete_column('funds_fundofficer', 'status')

        # Deleting field 'FundOfficer.notes'
        db.delete_column('funds_fundofficer', 'notes')

        # Deleting field 'FundOfficer.updated_by'
        db.delete_column('funds_fundofficer', 'updated_by_id')


        # Renaming column for 'FundOfficer.position' to match new field type.
        db.rename_column('funds_fundofficer', 'position', 'position_id')
        # Changing field 'FundOfficer.position'
        db.alter_column('funds_fundofficer', 'position_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funds.Position']))

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
            'effective_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fund': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fund_officers'", 'to': "orm['funds.Fund']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'officer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.OfficerDirector']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', 'no_check_for_status': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
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
            'effective_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fund': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'service_manager'", 'to': "orm['funds.Fund']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'service_manager': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.ServiceManager']"}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', 'no_check_for_status': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
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
            'effective_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issuer_officers'", 'to': "orm['funds.Issuer']"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'officer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funds.OfficerDirector']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', 'no_check_for_status': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'funds.servicemanager': {
            'Meta': {'ordering': "('name', 'country')", 'object_name': 'ServiceManager'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
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