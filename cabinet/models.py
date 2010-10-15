from django.db import models
from django.contrib.auth.models import User
from datetime import date

class CabinetProfile(models.Model):
	user = models.ForeignKey(User)
	credit = models.DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
		return "W%s" % (self.user.user.username) 

class Item(models.Model):
	name = models.CharField(max_length=100)
	cost = models.DecimalField(max_digits=5, decimal_places=2)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	img = models.ImageField(upload_to="items/")

	def __unicode__(self):
		return "%s($%.2f)" % (self.name, self.price)

class Receipt(models.Model):
	user = models.ForeignKey(CabinetProfile)
	date = models.DateField(auto_now=True)
	total = models.DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
		return "%s - %s" % (self.user.user.username, self.date.strftime("%m/%d/%Y"))

class ReceiptItem(models.Model):
	receipt = models.ForeignKey(Receipt)
	item = models.ForeignKey(Item)
	quantity = models.IntegerField()
	
	def __unicode__(self):
		return "%s (%d)" % (self.item.name, self.quantity)


