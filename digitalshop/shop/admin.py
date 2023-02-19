from django.contrib import admin

# Register your models here.
from .models import Product,Category,Payment,UserProduct

admin.site.register(Category)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(UserProduct)
