from django.views.generic import DetailView, ListView
from pages.models import Page
from posts.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    paginate_by = 10
    ordering = ['-pk']

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser or user.groups.filter(name='Editor'):
                return queryset
            else:
                return queryset.filter(author=user)
        else:
            return queryset.filter(status='PUBLISHED')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog!'
        context['blog_active'] = 'active'
        context['blog_active_link'] = '#'
        context['blog_active_sr'] = '<span class="sr-only">(current)</span>'
        if Page.objects.filter(slug='blog', status='PUBLISHED'):
            context['blog_page'] = Page.objects.get(slug='blog')
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser or user.groups.filter(name='Editor'):
                return queryset
            else:
                return queryset.filter(author=user)
        else:
            return queryset.filter(status='PUBLISHED')
