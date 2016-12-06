from django.contrib import admin

# Register your models here.
from shopping.models import Cart,Customer,BankDetail,Items

#admin.site.register(CustomerDetails)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(BankDetail)
admin.site.register(Items)
