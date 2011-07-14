# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Session'
        db.create_table('django_session', (
            ('session_key', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True)),
            ('session_data', self.gf('django.db.models.fields.TextField')()),
            ('expire_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('sessions', ['Session'])

    def backwards(self, orm):
        
        # Deleting model 'Session'
        db.delete_table('django_session')

    models = {
        'sessions.session': {
            'Meta': {'object_name': 'Session', 'db_table': "'django_session'"},
            'expire_date': ('django.db.models.fields.DateTimeField', [], {}),
            'session_data': ('django.db.models.fields.TextField', [], {}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'})
        }
    }

    complete_apps = ['sessions']
