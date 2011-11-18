# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Region'
        db.create_table('coffee_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('coffee', ['Region'])

        # Adding model 'Origin'
        db.create_table('coffee_origin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('farm', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coffee.Region'])),
            ('farmURL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('farmLogo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('hint', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('decaf', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wholesaleprice', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal('coffee', ['Origin'])

        # Adding model 'Roast'
        db.create_table('coffee_roast', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='25')),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('coffee', ['Roast'])

        # Adding model 'Batch'
        db.create_table('coffee_batch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('batch_id', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coffee.Origin'])),
            ('roast', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coffee.Roast'])),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('coffee', ['Batch'])


    def backwards(self, orm):
        
        # Deleting model 'Region'
        db.delete_table('coffee_region')

        # Deleting model 'Origin'
        db.delete_table('coffee_origin')

        # Deleting model 'Roast'
        db.delete_table('coffee_roast')

        # Deleting model 'Batch'
        db.delete_table('coffee_batch')


    models = {
        'coffee.batch': {
            'Meta': {'object_name': 'Batch'},
            'batch_id': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coffee.Origin']"}),
            'roast': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coffee.Roast']"})
        },
        'coffee.origin': {
            'Meta': {'object_name': 'Origin'},
            'decaf': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'farm': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'farmLogo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'farmURL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'hint': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coffee.Region']"}),
            'wholesaleprice': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        'coffee.region': {
            'Meta': {'object_name': 'Region'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'coffee.roast': {
            'Meta': {'object_name': 'Roast'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'25'"})
        }
    }

    complete_apps = ['coffee']
