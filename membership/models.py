from django.db import models
from django.contrib.auth.models import User
from datetime import date

CHOICES = (
	(1, "No Payment"),
	(2, "Online Payment"),
	(3, "Cash Payment"),
)

class Member(models.Model):
	payment = models.IntegerField(choices=CHOICES)
	user = models.ForeignKey(User)
