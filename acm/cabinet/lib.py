from acm.cabinet.models import *
from decimal import *

def get_profile(wnumber):
	try:
		return UserProfile.objects.get(user__username=wnumber)
	except UserProfile.DoesNotExist:
		u, created = User.objects.get_or_create(username=wnumber)
		if created:
			u.set_unusable_password()
			u.save()
		p, created = UserProfile.objects.get_or_create(user=u, credit=Decimal('0.00'))
		return p

def cart_total(cart):
	total = Decimal('0.0')
	items = Item.objects.in_bulk( map(int, cart.keys()) )
	for item_id, cart_item in cart.items():
		item = items[ int(item_id) ]
		total += item.price * cart_item['quantity']
	return total
