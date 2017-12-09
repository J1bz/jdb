from django.contrib import admin

from media.models import MediaCategory, MediaCategoryForm, Movie, MovieForm


class MediaCategoryAdmin(admin.ModelAdmin):
    form = MediaCategoryForm
    list_display = ('name', 'note',)
    search_fields = ('name', 'note',)


class MovieAdmin(admin.ModelAdmin):
    form = MovieForm
    list_display = (
        'title',
        'get_category_list',
        'realisator',
        'rating',
        'to_watch_again',
        'seen',
    )
    search_fields = ('title', 'categories__name', 'realisator', 'note',)

    def get_category_list(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])

    get_category_list.short_description = 'categories'


admin.site.register(MediaCategory, MediaCategoryAdmin)
admin.site.register(Movie, MovieAdmin)
