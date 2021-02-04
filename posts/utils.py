from django.utils.text import slugify


def process_slug(self, i):
    i += 1
    if self._meta.model_name == 'post':
        from posts.models import Post
        slug_filter = Post.objects.filter(slug__exact=self.slug)
    elif self._meta.model_name == 'page':
        from pages.models import Page
        slug_filter = Page.objects.filter(slug__exact=self.slug)
    if len(slug_filter) == 1:
        if not slug_filter[0].pk == self.pk:
            self.slug = f"{slugify(self.title)}-{i}"
            process_slug(self, i)


def get_unique_slug(self):
    if not self.slug:
        self.slug = slugify(self.title)
        i = 1
        process_slug(self, i)
