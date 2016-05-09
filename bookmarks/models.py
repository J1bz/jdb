from django.db.models import Model, CharField, ForeignKey, BooleanField
from django.forms import ModelForm, CharField as formCharField, Textarea

from common.models import Category


class Bookmark(Model):
    category = ForeignKey(Category)
    name = CharField(max_length=256, primary_key=True)
    note = CharField(max_length=256)


class BookmarkForm(ModelForm):
    note = formCharField(required=False, widget=Textarea)

    class Meta:
        model = Bookmark
        fields = ('category', 'name', 'note',)


class Book(Model):
    category = ForeignKey(Category)
    title = CharField(max_length=64, primary_key=True)
    author = CharField(max_length=64)
    note = CharField(max_length=256)
    read = BooleanField(default=False)


class BookForm(ModelForm):
    note = formCharField(required=False, widget=Textarea)

    class Meta:
        model = Book
        fields = ('category', 'title', 'author', 'note', 'read',)


class ReadLater(Model):
    category = ForeignKey(Category)
    name = CharField(max_length=256)
    note = CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'reads later'


class ReadLaterForm(ModelForm):
    note = formCharField(required=False, widget=Textarea)

    class Meta:
        model = ReadLater
        fields = ('category', 'name', 'note',)


class News(Model):
    category = ForeignKey(Category)
    name = CharField(max_length=256)
    rss = CharField(max_length=256, null=True)
    note = CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'news'


class NewsForm(ModelForm):
    note = formCharField(required=False, widget=Textarea)
    rss = formCharField(required=False)

    class Meta:
        model = News
        fields = ('category', 'name', 'rss', 'note',)


class People(Model):
    """Interesting people *.*"""
    category = ForeignKey(Category)
    name = CharField(max_length=256, primary_key=True)
    note = CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'people'


class PeopleForm(ModelForm):
    note = formCharField(required=False, widget=Textarea)

    class Meta:
        model = People
        fields = ('category', 'name', 'note',)
