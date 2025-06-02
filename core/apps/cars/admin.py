from django.contrib import admin
from . import models

admin.site.register(models.CarModel)
admin.site.register(models.CarType)
admin.site.register(models.CarMark)
admin.site.register(models.CarGeneration)
admin.site.register(models.DealType)
admin.site.register(models.CarOwner)
admin.site.register(models.Custom)
admin.site.register(models.Availability)
admin.site.register(models.Region)
admin.site.register(models.VehicleType)



class CarImageInline(admin.StackedInline):
    model = models.CarImage
    extra = 1

@admin.register(models.CarPost)
class CarPostModelAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    list_display = ['id']