from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms


class MediaCategory(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    note = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'media categories'

    def __str__(self):
        return self.name


class MediaCategoryForm(forms.ModelForm):
    note = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = MediaCategory
        fields = '__all__'


class Movie(models.Model):
    categories = models.ManyToManyField(MediaCategory)
    title = models.CharField(max_length=64, primary_key=True)
    realisator = models.CharField(max_length=64)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    to_watch_again = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    note = models.CharField(max_length=1024)
    seen = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class MovieForm(forms.ModelForm):
    note = forms.CharField(required=False, widget=forms.Textarea)
    realisator = forms.CharField(required=False)

    class Meta:
        model = Movie
        fields = '__all__'
