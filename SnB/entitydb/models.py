from django.db import models

# Create your models here.
class Entity(models.Model):
	def __unicode__(self):
		if self.organization_name:
			return self.organization_name
		else:
			return self.first_name + " " + self.last_name

	class Meta:
		verbose_name_plural = "Entities"

	first_name = models.CharField(max_length=100, blank=True)	
	last_name = models.CharField(max_length=100, blank=True)	
	organization_name = models.CharField(max_length=100, blank=True)
	affiliated_with = models.ForeignKey('self', blank=True, null=True)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	rolls = models.ManyToManyField('Roll', through='Membership', blank=True, null=True)
	zip = models.CharField(max_length=10)

class Organization(models.Model):
	def __unicode__(self):
		return self.name

	entity = models.ForeignKey('Entity')
	tin = models.CharField(max_length=11, blank=True)

class Roll(models.Model):
	def __unicode__(self):
		return self.name

	name = models.CharField(max_length=127)
	description = models.TextField()

class Membership(models.Model):
	def __unicode__(self):
		return self.roll.name + ' - ' + self.entity.first_name + ' ' + self.entity.last_name

	entity = models.ForeignKey(Entity)
	roll = models.ForeignKey(Roll)
	date_started = models.DateField()
	date_ended = models.DateField(blank=True, null=True)
	tin = models.CharField(max_length=11, blank=True, null=True)
