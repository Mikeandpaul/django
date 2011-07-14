# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ContentType'
        db.create_table('django_content_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('app_label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('contenttypes', ['ContentType'])

        # Adding unique constraint on 'ContentType', fields ['app_label', 'model']
        db.create_unique('django_content_type', ['app_label', 'model'])

    def backwards(self, orm):
        
        # Removing unique constraint on 'ContentType', fields ['app_label', 'model']
        db.delete_unique('django_content_type', ['app_label', 'model'])

        # Deleting model 'ContentType'
        db.delete_table('django_content_type')

    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contenttypes']
