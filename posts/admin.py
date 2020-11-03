from .models import Post, PostCategory
from django import forms
from django.contrib import admin
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
