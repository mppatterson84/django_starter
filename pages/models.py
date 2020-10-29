from django.db import models
from django.urls import reverse
from posts.base_models import PostBase


class Page(PostBase):
    add_to_menu = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={'slug': self.slug})
