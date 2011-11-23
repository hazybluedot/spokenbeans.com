from django.db import models
from SnB.coffee.prices import getRetailPrice, addTax

# Create your models here.

class Region(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Origin(models.Model):
    def __unicode__(self):
        return self.name

    @staticmethod
    def get_choices():
        choices = ()
        for origin in Origin.objects.all():
            choices += ( (origin.short_name(), origin), )
        return choices

    def short_name(self):
        return self.name.lower().replace(" ", "_")

    def get_hint(self):
        if self.hint:
            return self.hint
        else:
            return self.region

    def get_prices(self):
            price_list = ()
            price_list += ( addTax(getRetailPrice(float(self.wholesaleprice), 0.77, 0.75), 1.025), )
            price_list += ( addTax(getRetailPrice(float(self.wholesaleprice), 0.38, 0.85), 1.025), )
            price_list += ( 14, )
            price_list += ( 7, )
            return price_list

    name = models.CharField(max_length=100)
    farm = models.CharField(max_length=200)
    region = models.ForeignKey('Region')
    farmURL = models.URLField(blank=True)
    farmLogo = models.ImageField(upload_to='logos', blank=True)
    hint = models.TextField(blank=True)
    description = models.TextField(blank=True)
    decaf = models.BooleanField(default=False)
    blend = models.BooleanField(default=False)
    wholesaleprice = models.DecimalField(max_digits=4, decimal_places=2)

class Roast(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length="25")
    description = models.TextField()

class Batch(models.Model):
    def __unicode__(self):
        return self.id

    batch_id = models.IntegerField()
    date = models.DateField()
    origin = models.ForeignKey('Origin')
    roast = models.ForeignKey('Roast')
    notes = models.TextField(blank=True)

