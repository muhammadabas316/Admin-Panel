from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
class spare_part_admin(admin.ModelAdmin):
    list_display = ('name','vehicle','price','photo_tag','in_stock',)
    list_filter = ('in_stock',)


    def photo_tag(self, obj):
        return format_html(f'<img src ="/media/{obj.image}" style="height:50px,width:50px">')


admin.site.register(spare_part,spare_part_admin)