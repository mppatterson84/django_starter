from .models import Post, PostCategory
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(
        widget=CKEditorWidget()
    )
    slug = forms.CharField(
        help_text='Leave blank to have a slug generated automatically.',
        required=False
    )
    categories = forms.ModelMultipleChoiceField(
        queryset=PostCategory.objects.all(),
        help_text='Hold ctrl or cmd to select multiple categories.',
        required=False,
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'author',
            'created_at',
            'updated_at',
            'slug',
            'status',
            'categories',
        ]


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    def get_queryset(self, request):
        """
        Show only a user's own posts if the
        user is not a superuser or 'Editor'.
        """
        q = super().get_queryset(request)
        current_user = request.user
        if current_user.is_superuser or current_user.groups.filter(name='Editor'):
            return q
        return q.filter(author=current_user)

    def get_form(self, request, obj=None, **kwargs):
        """
        Have the current user selected initially.
        """
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
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


class PostCategoryAdminForm(forms.ModelForm):
    category_name = forms.CharField()

    class Meta:
        model = PostCategory
        fields = [
            'category_name',
        ]


class PostCategoryAdmin(admin.ModelAdmin):
    form = PostCategoryAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
