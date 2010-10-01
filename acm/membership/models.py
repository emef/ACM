from django.db import models
from django.contrib.auth.models import User
from datetime import date

#user.username = WNumber
class member(models.Model):
    user = models.ForeignKey(User)
    paid_with_cash = models.BooleanField()
    pending_payment = models.BooleanField()
    
