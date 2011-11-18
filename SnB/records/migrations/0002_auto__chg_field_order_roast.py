# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Order.roast'
        db.alter_column('records_order', 'roast_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Roast'], null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Order.roast'
        raise RuntimeError("Cannot reverse this migration. 'Order.roast' and its values cannot be restored.")


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
            'roast': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Roast']", 'null': 'True', 'blank': 'True'}),
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
