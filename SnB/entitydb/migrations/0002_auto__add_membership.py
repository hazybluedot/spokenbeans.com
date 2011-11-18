# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Membership'
        db.create_table('entitydb_membership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entitydb.Entity'])),
            ('roll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entitydb.Roll'])),
            ('date_started', self.gf('django.db.models.fields.DateField')()),
            ('date_ended', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('tin', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
        ))
        db.send_create_signal('entitydb', ['Membership'])

        # Removing M2M table for field rolls on 'Entity'
        db.delete_table('entitydb_entity_rolls')


    def backwards(self, orm):
        
        # Deleting model 'Membership'
        db.delete_table('entitydb_membership')

        # Adding M2M table for field rolls on 'Entity'
        db.create_table('entitydb_entity_rolls', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entity', models.ForeignKey(orm['entitydb.entity'], null=False)),
            ('roll', models.ForeignKey(orm['entitydb.roll'], null=False))
        ))
        db.create_unique('entitydb_entity_rolls', ['entity_id', 'roll_id'])


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
            'rolls': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['entitydb.Roll']", 'null': 'True', 'through': "orm['entitydb.Membership']", 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'entitydb.membership': {
            'Meta': {'object_name': 'Membership'},
            'date_ended': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_started': ('django.db.models.fields.DateField', [], {}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entitydb.Entity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roll': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entitydb.Roll']"}),
            'tin': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'})
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
