from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from pages.models import Page
from ckeditor.widgets import CKEditorWidget

# Register your models here.


class PageAdminForm(forms.ModelForm):
    body = forms.CharField(
        widget=CKEditorWidget()
    )

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

    def get_form(self, request, obj=None, **kwargs):
        """
        Have the current user selected initially.
        """
        form = super(PageAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        return form

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Show only the current user if not a superuser or 'Editor'.
        """
        current_user = request.user
        user_queryset = User.objects.filter(username=current_user)
        if current_user.is_superuser or current_user.groups.filter(name='Editor'):
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        elif db_field.name == 'author':
            kwargs['queryset'] = user_queryset
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Page, PageAdmin)
