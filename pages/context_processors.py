from pages.models import Page


def base(request):
    context = dict()
    if Page.objects.filter(add_to_menu=True, status='PUBLISHED'):
        context['menu_items'] = Page.objects.filter(
            add_to_menu=True, status='PUBLISHED').order_by('pk')
    return context
