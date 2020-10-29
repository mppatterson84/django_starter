from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from posts.base_models import PostBase


class Post(PostBase):
    categories = models.ManyToManyField('posts.PostCategory')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})


class PostCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=False, blank=True, default='slug')

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(PostCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Post Categories"

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug, })
