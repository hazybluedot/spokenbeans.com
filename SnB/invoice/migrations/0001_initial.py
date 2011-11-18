# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Invoice'
        db.create_table('invoice_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender', to=orm['entitydb.Entity'])),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipient', to=orm['entitydb.Entity'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('invoice', ['Invoice'])

        # Adding model 'Transaction'
        db.create_table('invoice_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('payer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='payer', to=orm['entitydb.Entity'])),
            ('payee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='payee', to=orm['entitydb.Entity'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('payment_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('meta', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoice.Invoice'], null=True, blank=True)),
        ))
        db.send_create_signal('invoice', ['Transaction'])


    def backwards(self, orm):
        
        # Deleting model 'Invoice'
        db.delete_table('invoice_invoice')

        # Deleting model 'Transaction'
        db.delete_table('invoice_transaction')


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
        'invoice.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipient'", 'to': "orm['entitydb.Entity']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'to': "orm['entitydb.Entity']"})
        },
        'invoice.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoice.Invoice']", 'null': 'True', 'blank': 'True'}),
            'meta': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'payee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'payee'", 'to': "orm['entitydb.Entity']"}),
            'payer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'payer'", 'to': "orm['entitydb.Entity']"}),
            'payment_type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['invoice']
