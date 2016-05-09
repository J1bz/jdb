from django.contrib import admin
from bookmarks.models import (
    Bookmark, BookmarkForm, Book, BookForm, ReadLater, ReadLaterForm,
    News, NewsForm, People, PeopleForm)


class BookmarkAdmin(admin.ModelAdmin):
    form = BookmarkForm
    list_display = ('category', 'name', 'note',)
    search_fields = ('category__name', 'name', 'note',)


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('category', 'title', 'author', 'note', 'read',)
    search_fields = ('category__name', 'title', 'author', 'note',)


class ReadLaterAdmin(admin.ModelAdmin):
    form = ReadLaterForm
    list_display = ('category', 'name', 'note',)
    search_fields = ('category__name', 'name', 'note',)


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ('category', 'name', 'rss', 'note',)
    search_fields = ('category__name', 'name', 'note',)


class PeopleAdmin(admin.ModelAdmin):
    form = PeopleForm
    list_display = ('category', 'name', 'note',)
    search_fields = ('category__name', 'name', 'note',)

admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(ReadLater, ReadLaterAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(People, PeopleAdmin)
