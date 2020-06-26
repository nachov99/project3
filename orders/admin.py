from django.contrib import admin
from .models import pizza, topping, sub, pasta, salad, DinnerPlatter

# Register your models here.
admin.site.register(pizza)
admin.site.register(topping)
admin.site.register(sub)
admin.site.register(pasta)
admin.site.register(salad)
admin.site.register(DinnerPlatter)
