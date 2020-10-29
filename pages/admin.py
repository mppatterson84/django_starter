from django import forms
from django.contrib import admin
from pages.models import Page

# Register your models here.


class PageAdminForm(forms.ModelForm):
    slug = forms.CharField(
        help_text='Leave blank to have a slug generated automatically.',
        required=False
    )
    add_to_menu = forms.BooleanField(
        help_text='Check the box to add this page to the main menu. The page status must be published to show in the menu.',
        required=False)

    class Meta:
        model = Page
        fields = [
            'title',
            'body',
            'author',
            'slug',
            'status',
            'add_to_menu',
        ]


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm


admin.site.register(Page, PageAdmin)
