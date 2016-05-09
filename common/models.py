from django.db.models import Model, CharField
from django.forms import ModelForm, CharField as formCharField, Textarea


class Category(Model):
    name = CharField(max_length=32, primary_key=True)
    note = CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class CategoryForm(ModelForm):
    note = formCharField(required=False, widget=Textarea)

    class Meta:
        model = Category
        fields = ('name', 'note',)
