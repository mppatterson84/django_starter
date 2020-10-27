from django import forms
from django.contrib import admin
from django.contrib.sites.shortcuts import get_current_site
from pages.models import Page
from urllib import request

# Register your models here.


class PageAdminForm(forms.ModelForm):
    slug = forms.CharField(
        help_text=f'Example: {get_current_site(request).domain}/my-slug/')
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
