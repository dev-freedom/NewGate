from django.views import generic
from products.models import Product

# View for Home page
class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ProductAbout(generic.TemplateView):
    template_name = 'about.html'


class ProductContact(generic.TemplateView):
    template_name = 'contact.html'
