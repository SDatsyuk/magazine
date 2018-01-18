from django.contrib import admin
from .models import *

######################################################################
class OrderProductInLine(admin.TabularInline):
	model = OrderProduct
	extra = 0


class OrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Order._meta.fields]
	inlines = [OrderProductInLine]

	class Meta:
		model = Order

admin.site.register(Order, OrderAdmin)

########################################################################

admin.site.register(OrderProduct)
admin.site.register(OrderStatus)