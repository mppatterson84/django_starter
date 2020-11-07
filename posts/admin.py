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

    def get_queryset(self, request):
        """
        Show only a user's own posts if the 
        user is not a superuser or 'Editor'.
        """
        q = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name='Editor'):
            return q
        return q.filter(author=request.user)


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


# class PostAdminFilter(admin.ModelAdmin):
#     def get_queryset(self, request):
#         """
#         filter the objects to show only those created by a user
#         """
#         q = super().get_queryset(request)
#         if request.user.is_superuser:
#             return q
#         return q.filter(author=request.user)
