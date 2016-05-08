from django.contrib import admin
from common.models import Category, CategoryForm


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ('name', 'note',)
    search_fields = ('name', 'note',)

admin.site.register(Category, CategoryAdmin)
