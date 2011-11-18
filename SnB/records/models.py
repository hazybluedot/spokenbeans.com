from django.db import models
from SnB.entitydb.models import Entity
from SnB.coffee.models import *

# Create your models here.
#class Supplier(models.Model):
#    def __unicode__(self):
#        return self.entity
#
#    class Meta:
#        verbose_name_plural = "Companies"
#        entity = models.OneToOneField('entitydb.Entity', related_name='company')
#        tin = models.CharField(max_length=100, blank=True)



class Rating(models.Model):
    RATING_CHOICES = (
            (1,1), 
            (2,2),
            (3,3),
            (4,4),
            (5,5),
            )
    customer = models.ForeignKey('entitydb.Entity')
    batch = models.ForeignKey('coffee.Batch')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.CharField(max_length="255")
#class Variety(models.Model)
#	origin = models.ForeignKey('Origin')

# do we need a specific pulls object or should "pulls" just be a view?
class Pull(models.Model):
    def __unicode__(self):
        return self.date

    jar = models.ManyToManyField('Jar')
    date = models.DateField()

class Jar(models.Model):
    def __unicode__(self):
        return self.origin + self.roastLevel

    order = models.ForeignKey('Order')
    origin = models.ForeignKey('coffee.Origin')
    roastLevel = models.ForeignKey('coffee.Roast')
    batch = models.ForeignKey('coffee.Batch')
    date_filled = models.DateField()
    size = models.DecimalField(max_digits=2,decimal_places=1)
    weight = models.DecimalField(max_digits=4,decimal_places=2)

def dated_name(obj, date):
    ent = obj.id_entity
    name = ent.last_name + ", " + ent.first_name + " - " + date.__str__()
    return name

class Subscription(models.Model):
    def __unicode__(self):
        return dated_name(self, self.date_started)

    FREQUENCY_CHOICES = (
            (u'W', u'Weekly'), 
            (u'B', u'Biweekly'), 
            (u'Q', u'Quaterweekly'),
            )

    SIZE_CHOICES = (
            (0.5, u'Pint'),
            (1, u'Quart'),
            )

    STATUS_CHOICES = (
            ('A','Active'),
            ('H','Hold'),
            ('C','Canceled'),
            )

    id_entity = models.ForeignKey('entitydb.Entity')
    date_started = models.DateField('Start Date')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    roast = models.ForeignKey('coffee.Roast', null=True, blank=True)
    origin = models.ForeignKey('coffee.Origin', null=True, blank=True)
    region = models.ForeignKey('coffee.Region', null=True, blank=True)
    frequency = models.CharField(max_length=2, choices=FREQUENCY_CHOICES)
    size = models.DecimalField(max_digits=2,decimal_places=1)

    def is_active(self):
        return self.status=='A'

class Order(models.Model):
    def __unicode__(self):
        return dated_name(self, self.date_placed)

    id_entity = models.ForeignKey('entitydb.Entity')
    date_placed = models.DateField()
    date_fulfilled = models.DateField(null=True, blank=True)
    subscription = models.ForeignKey('Subscription', null=True, blank=True)
    roast = models.ForeignKey('coffee.Roast', null=True, blank=True)
    origin = models.ForeignKey('coffee.Origin', null=True, blank=True)
    region = models.ForeignKey('coffee.Region', null=True, blank=True)
    size = models.DecimalField(max_digits=2,decimal_places=1)


class Runner(models.Model):
    def __unicode__(self):
        return self.person.get_full_name()

    person = models.OneToOneField('entitydb.Entity')
    tin = models.CharField(max_length=11)
    date_started = models.DateField()
    date_ended = models.DateField(blank=True, null=True)

class Delivery(models.Model):
    def __unicode__(self):
        return self.name
#    class Meta:
#        verbose_name_plural="Deliveries"

        id_entity = models.ForeignKey('entitydb.Entity')
        id_order = models.ForeignKey('Order')
        id_runner = models.ForeignKey('Runner')
        date = models.DateField()
