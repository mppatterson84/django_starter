from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView
from pages.models import Page
import os


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Homepage!'
        context['home_active'] = 'active'
        context['home_active_link'] = '#'
        context['home_active_sr'] = '<span class="sr-only">(current)</span>'
        if Page.objects.filter(slug='home', status='PUBLISHED'):
            context['home_page'] = Page.objects.get(slug='home')
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_authenticated and queryset.filter(author=self.request.user):
            return queryset
        else:
            queryset = queryset.filter(status='PUBLISHED')
            return queryset


class BrowserPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/browser.html'
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Browser'
        context['browser_active'] = 'active'
        context['browser_active_link'] = '#'
        context['browser_active_sr'] = '<span class="sr-only">(current)</span>'
        context['cloud_name'] = os.environ.get('CLOUD_NAME')
        context['api_key'] = os.environ.get('API_KEY')
        context['user_name'] = os.environ.get('CLOUDINARY_USER')
        return context
