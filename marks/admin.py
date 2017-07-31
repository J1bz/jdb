from django.contrib import admin
from django.utils.html import format_html
from marks.models import (
    Bookmark, BookmarkForm, Book, BookForm, ReadLater, ReadLaterForm,
    News, NewsForm, People, PeopleForm)


class HyperlinkedNameMixin():
    def hyperlinked_name(self, obj):
        return format_html("<a href='{0}'>{0}</a>".format(obj))

    hyperlinked_name.allow_tags = True


class BookmarkAdmin(HyperlinkedNameMixin, admin.ModelAdmin):
    form = BookmarkForm
    list_display = ('category', 'hyperlinked_name', 'note',)
    search_fields = ('category__name', 'name', 'note',)


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('category', 'title', 'author', 'note', 'read',)
    search_fields = ('category__name', 'title', 'author', 'note',)


class ReadLaterAdmin(HyperlinkedNameMixin, admin.ModelAdmin):
    form = ReadLaterForm
    list_display = ('category', 'hyperlinked_name', 'note',)
    search_fields = ('category__name', 'name', 'note',)


class NewsAdmin(HyperlinkedNameMixin, admin.ModelAdmin):
    form = NewsForm
    list_display = ('category', 'hyperlinked_name', 'rss', 'note',)
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
