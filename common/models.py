from django.db.models import Model, CharField
from django.forms import ModelForm, CharField as formCharField, Textarea


class Category(Model):
    name = CharField(max_length=32, primary_key=True)
    description = CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'categories'


class CategoryForm(ModelForm):
    description = formCharField(required=False, widget=Textarea)

    class Meta:
        model = Category
        fields = ('name', 'description',)
