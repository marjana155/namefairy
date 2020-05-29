from django.contrib import admin
from .models import Name, Category, Gender
# Register your models here.


class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'gender')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)


class GenderAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Name, NameAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gender, GenderAdmin)
