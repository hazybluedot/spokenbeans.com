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
            price_list += ( addTax(getRetailPrice(float(self.wholesaleprice), 0.77, 0.75), 0.025), )
            price_list += ( addTax(getRetailPrice(float(self.wholesaleprice), 0.38, 0.85), 0.025), )
            return price_list

    name = models.CharField(max_length=100)
    farm = models.CharField(max_length=200)
    region = models.ForeignKey('Region')
    farmURL = models.URLField(blank=True)
    farmLogo = models.ImageField(upload_to='logos', blank=True)
    #trade = models.CharField(max_length=100, blank=True, choices=(('direct','Direct'), ('other','Other/Unknown')), null=True)
    #altitude = models.IntegerField(blank=True, help_text="Feet above sealevel", default=-1)
    #acidity = models.IntegerField(blank=True, choices=(('1','Low'),('2','Medium'),('3','High')), null=True)
    #body = models.IntegerField(blank=True, choices=(('1','Light'),('2','Medium'),('3','Full')), null=True)
    hint = models.TextField(blank=True)
    description = models.TextField(blank=True)
    decaf = models.BooleanField(default=False)
    blend = models.BooleanField(default=False)
    available = models.BooleanField(default=False)
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

