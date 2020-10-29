from django.db import models
from django.urls import reverse
from django.utils import timezone
from posts.utils import get_unique_slug


class PostBase(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(
        'auth.User', default='auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    updated_at = models.DateTimeField(default=timezone.now, blank=False)
    slug = models.SlugField(blank=True, unique=True,)
    DRAFT = 'DRAFT'
    PENDING_REVIEW = 'PENDING_REVIEW'
    PUBLISHED = 'PUBLISHED'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PENDING_REVIEW, 'Pending Review'),
        (PUBLISHED, 'Published'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        get_unique_slug(self)
        self.updated_at = timezone.now()
        super(PostBase, self).save(*args, **kwargs)
