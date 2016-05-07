from django.contrib import admin
from common.models import Category, CategoryForm


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)

admin.site.register(Category, CategoryAdmin)
