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

def make_purchase(profile, cart):
	items = Item.objects.in_bulk( map(int, cart.keys()) )
	total = Decimal('0.0')

	#calculate total so we don't have to make 2 queries by calling calc_total
	for item_id, cart_item in cart.items():
		item = items[ int(item_id) ]
		total += item.price * cart_item['quantity']

	#subtract total from users account
	profile.credit -= total
	profile.save()

	#create the receipt now that we have the total
	receipt = Receipt.objects.create(user=profile, total=total)

	#create a receiptItem for each item in the cart
	for item_id, cart_item in cart.items():
		item = items[ int(item_id) ]
		quantity = int( cart_item['quantity'])
		receipt.receiptitem_set.create(item=item, quantity=quantity)

	return receipt
