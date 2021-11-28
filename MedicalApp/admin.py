from django.contrib import admin
from MedicalApp.models import MedicalData
# Register your models here.
class MedicalDataAdmin(admin.ModelAdmin):
    list_display=['sku_id','product_id','sku_name']

admin.site.register(MedicalData,MedicalDataAdmin)
