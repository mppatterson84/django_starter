from django.views.generic import TemplateView, DetailView
from pages.models import Page


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
