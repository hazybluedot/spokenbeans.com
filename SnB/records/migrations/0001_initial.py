# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Supplier'
        db.create_table('records_supplier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.OneToOneField')(related_name='company', unique=True, to=orm['entitydb.Entity'])),
            ('tin', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('records', ['Supplier'])

        # Adding model 'Region'
        db.create_table('records_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('records', ['Region'])

        # Adding model 'Origin'
        db.create_table('records_origin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('farm', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Region'])),
            ('farmURL', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('farmLogo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('records', ['Origin'])

        # Adding model 'Batch'
        db.create_table('records_batch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('batch_id', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Origin'])),
            ('roast', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Roast'])),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('records', ['Batch'])

        # Adding model 'Rating'
        db.create_table('records_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entitydb.Entity'])),
            ('batch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Batch'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length='255')),
        ))
        db.send_create_signal('records', ['Rating'])

        # Adding model 'Pull'
        db.create_table('records_pull', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('records', ['Pull'])

        # Adding M2M table for field jar on 'Pull'
        db.create_table('records_pull_jar', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pull', models.ForeignKey(orm['records.pull'], null=False)),
            ('jar', models.ForeignKey(orm['records.jar'], null=False))
        ))
        db.create_unique('records_pull_jar', ['pull_id', 'jar_id'])

        # Adding model 'Jar'
        db.create_table('records_jar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Order'])),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Origin'])),
            ('roastLevel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Roast'])),
            ('batch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Batch'])),
            ('date_filled', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('records', ['Jar'])

        # Adding model 'Subscription'
        db.create_table('records_subscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entitydb.Entity'])),
            ('date_started', self.gf('django.db.models.fields.DateField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('roast', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Roast'], null=True, blank=True)),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Origin'], null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Region'], null=True, blank=True)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('size', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
        ))
        db.send_create_signal('records', ['Subscription'])

        # Adding model 'Order'
        db.create_table('records_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entitydb.Entity'])),
            ('date_placed', self.gf('django.db.models.fields.DateField')()),
            ('date_fulfilled', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('subscription', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Subscription'], null=True, blank=True)),
            ('roast', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Roast'])),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Origin'], null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Region'], null=True, blank=True)),
        ))
        db.send_create_signal('records', ['Order'])

        # Adding model 'Roast'
        db.create_table('records_roast', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='25')),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('records', ['Roast'])

        # Adding model 'Runner'
        db.create_table('records_runner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['entitydb.Entity'], unique=True)),
            ('tin', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('date_started', self.gf('django.db.models.fields.DateField')()),
            ('date_ended', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('records', ['Runner'])

        # Adding model 'Delivery'
        db.create_table('records_delivery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entitydb.Entity'])),
            ('id_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Order'])),
            ('id_runner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Runner'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('records', ['Delivery'])


    def backwards(self, orm):
        
        # Deleting model 'Supplier'
        db.delete_table('records_supplier')

        # Deleting model 'Region'
        db.delete_table('records_region')

        # Deleting model 'Origin'
        db.delete_table('records_origin')

        # Deleting model 'Batch'
        db.delete_table('records_batch')

        # Deleting model 'Rating'
        db.delete_table('records_rating')

        # Deleting model 'Pull'
        db.delete_table('records_pull')

        # Removing M2M table for field jar on 'Pull'
        db.delete_table('records_pull_jar')

        # Deleting model 'Jar'
        db.delete_table('records_jar')

        # Deleting model 'Subscription'
        db.delete_table('records_subscription')

        # Deleting model 'Order'
        db.delete_table('records_order')

        # Deleting model 'Roast'
        db.delete_table('records_roast')

        # Deleting model 'Runner'
        db.delete_table('records_runner')

        # Deleting model 'Delivery'
        db.delete_table('records_delivery')


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
        'entitydb.roll': {
            'Meta': {'object_name': 'Roll'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'records.batch': {
            'Meta': {'object_name': 'Batch'},
            'batch_id': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Origin']"}),
            'roast': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Roast']"})
        },
        'records.delivery': {
            'Meta': {'object_name': 'Delivery'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entitydb.Entity']"}),
            'id_order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Order']"}),
            'id_runner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Runner']"})
        },
        'records.jar': {
            'Meta': {'object_name': 'Jar'},
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Batch']"}),
            'date_filled': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Order']"}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Origin']"}),
            'roastLevel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Roast']"})
        },
        'records.order': {
            'Meta': {'object_name': 'Order'},
            'date_fulfilled': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_placed': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entitydb.Entity']"}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Origin']", 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Region']", 'null': 'True', 'blank': 'True'}),
            'roast': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Roast']"}),
            'subscription': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Subscription']", 'null': 'True', 'blank': 'True'})
        },
        'records.origin': {
            'Meta': {'object_name': 'Origin'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'farm': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'farmLogo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'farmURL': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Region']"})
        },
        'records.pull': {
            'Meta': {'object_name': 'Pull'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['records.Jar']", 'symmetrical': 'False'})
        },
        'records.rating': {
            'Meta': {'object_name': 'Rating'},
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Batch']"}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entitydb.Entity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        'records.region': {
            'Meta': {'object_name': 'Region'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'records.roast': {
            'Meta': {'object_name': 'Roast'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'25'"})
        },
        'records.runner': {
            'Meta': {'object_name': 'Runner'},
            'date_ended': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_started': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['entitydb.Entity']", 'unique': 'True'}),
            'tin': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        },
        'records.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'date_started': ('django.db.models.fields.DateField', [], {}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entitydb.Entity']"}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Origin']", 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Region']", 'null': 'True', 'blank': 'True'}),
            'roast': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Roast']", 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'records.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'entity': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'company'", 'unique': 'True', 'to': "orm['entitydb.Entity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['records']
