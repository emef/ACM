from django import template

register = template.Library()

@register.filter
def currency(value):
	dollars = float(value)
	return "$%s" % ("%0.2f" % dollars)
