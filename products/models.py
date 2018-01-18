from django.db import models
from unidecode import unidecode
from django.template.defaultfilters import slugify


class Category(models.Model):
	title = models.CharField(max_length=50, blank=True, null=True, default=None)
	description = models.TextField(blank=True, null=True, default=None)
	#parent_category = models.ForeignKey(Category, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return '%s' % self.title


class Property(models.Model):
	category = models.ForeignKey(Category, blank=True, null=True, default=None)
	#id_product = models.ForeignKey(Product)
	name = models.CharField(max_length=250, blank=True, null=True, default=None)
	#product = models.ForeignKey()
	is_active = models.BooleanField(default=True)


	def __str__(self):
		return self.name


# Таблиця товарів
class Product(models.Model):
	title = models.CharField(max_length=128, blank=True, null=True, default=None)
	slug = models.SlugField(max_length=128, unique=True, blank=True, default=None, null=True)
	category = models.ForeignKey(Category, blank=True, null=True, default=None)
	description = models.TextField(blank=True, null=True, default=None)
	price = models.FloatField(blank=True, null=True, default=None)
	#product_property = models.ForeignKey(Property, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return '%s' % self.title

	def save(self):
		if not self.slug:
			self.slug = slugify(unidecode(self.title))
		super(Product, self).save()



# Значення характеристик товару
class PropertyValue(models.Model):
	product = models.ForeignKey(Product)
	property = models.ForeignKey(Property)
	value = models.CharField(max_length=100, blank=True, null=True, default=None)
	unit_of_measurement = models.CharField(max_length=16, blank=True, null=True, default=None)

	def __str__(self):
		return '%s' % self.value


# Зображення товарів
class ProductImage(models.Model):
	product = models.ForeignKey(Product, blank=True, null=True, default=None, related_name='images')
	image = models.ImageField(upload_to='products_images/')
	sort_order = models.IntegerField( blank=True, null=True, default=0)
	is_main = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return '%s' % self.id

	class Meta:
		ordering = ['sort_order']



