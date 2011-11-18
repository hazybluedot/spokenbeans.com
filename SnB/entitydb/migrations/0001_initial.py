# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Entity'
        db.create_table('entitydb_entity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('organization_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('affiliated_with', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entitydb.Entity'], null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('entitydb', ['Entity'])

        # Adding M2M table for field rolls on 'Entity'
        db.create_table('entitydb_entity_rolls', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entity', models.ForeignKey(orm['entitydb.entity'], null=False)),
            ('roll', models.ForeignKey(orm['entitydb.roll'], null=False))
        ))
        db.create_unique('entitydb_entity_rolls', ['entity_id', 'roll_id'])

        # Adding model 'Organization'
        db.create_table('entitydb_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entitydb.Entity'])),
            ('tin', self.gf('django.db.models.fields.CharField')(max_length=11, blank=True)),
        ))
        db.send_create_signal('entitydb', ['Organization'])

        # Adding model 'Roll'
        db.create_table('entitydb_roll', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('entitydb', ['Roll'])


    def backwards(self, orm):
        
        # Deleting model 'Entity'
        db.delete_table('entitydb_entity')

        # Removing M2M table for field rolls on 'Entity'
        db.delete_table('entitydb_entity_rolls')

        # Deleting model 'Organization'
        db.delete_table('entitydb_organization')

        # Deleting model 'Roll'
        db.delete_table('entitydb_roll')


    models = {
        'entitydb.entity': {
            'Meta': {'object_name': 'Entity'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'affiliated_with': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entitydb.Entity']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'organization_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'rolls': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['entitydb.Roll']", 'symmetrical': 'False'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'entitydb.organization': {
            'Meta': {'object_name': 'Organization'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entitydb.Entity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tin': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'})
        },
        'entitydb.roll': {
            'Meta': {'object_name': 'Roll'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        }
    }

    complete_apps = ['entitydb']
