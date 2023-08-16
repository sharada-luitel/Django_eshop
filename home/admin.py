from django.contrib import admin
from .models import *
# Register your models here.
admin.site.egister(Category)
admin.site.egister(Slider)
admin.site.egister(Brand)
admin.site.egister(Shop)
admin.site.egister(Ad)

