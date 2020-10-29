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
        if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
            return queryset
        else:
            queryset = queryset.filter(status='PUBLISHED')
        return queryset

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
