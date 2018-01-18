from django.contrib import admin
from .models import *
######################################################################
class PropertyValueInLine(admin.TabularInline):
	model = PropertyValue
	extra = 0


class ProductImageInLine(admin.TabularInline):
	model = ProductImage
	extra = 0


class ProductAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Product._meta.fields]
	inlines = [PropertyValueInLine, ProductImageInLine]

	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)

########################################################################


class ProductImageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ProductImage._meta.fields]
	
	class Meta:
		model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)
##########################################################################

class PropertyAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Property._meta.fields]
	
	class Meta:
		model = Property

admin.site.register(Property, PropertyAdmin)

###########################################################################

class PropertyValueAdmin(admin.ModelAdmin):
	list_display = [field.name for field in PropertyValue._meta.fields]

	class Meta:
		model = PropertyValue

admin.site.register(PropertyValue, PropertyValueAdmin)
########################################################################

class CategoryAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Category._meta.fields]

	class Meta:
		model = Category

admin.site.register(Category, CategoryAdmin)
