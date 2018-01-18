from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class OrderStatus(models.Model):
	title = models.CharField(max_length=256, blank=True, null=True, default=None)
	description = models.TextField(blank=True, null=True, default=None)

	def __str__(self):
		return '%s' % self.title


class Order(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, default=None)
	create = models.DateTimeField(auto_now_add=False, auto_now=True)
	order_price = models.FloatField(blank=True, null=True, default=None)
	status = models.ForeignKey(OrderStatus, blank=True, null=True, default=None)

	def __str__(self):
		return 'User: %s price: %s status: %s' % (self.user, self.order_price, self.status)



class OrderProduct(models.Model):
	order = models.ForeignKey(Order, blank=True, null=True, default=None)
	product = models.ForeignKey(Product, blank=True, null=True, default=None)
	num = models.IntegerField(blank=True, null=True, default=None)
	price = models.FloatField(blank=True, null=True, default=None)  #product.price
	total_price = models.FloatField(blank=True, null=True, default=None)  #self.product.price * self.num
	is_active = models.BooleanField(default=True)

	
	def save(self, *args, **kwargs):
		self.price = self.product.price
		self.total_price = self.num * self.price

		super(OrderProduct, self).save(*args, **kwargs)


def total_price_post_save(sender, instance, created, **kwargs):
	product_in_order = OrderProduct.objects.filter(order=instance.order, is_active=True)
	total_price = 0
	for item in product_in_order:
		total_price += item.total_price

	instance.order.order_price = total_price
	instance.order.save(force_update=True)

post_save.connect(total_price_post_save, sender=OrderProduct)