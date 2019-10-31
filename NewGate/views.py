from django.views import generic


# View for Home page
class IndexView(generic.TemplateView):
    template_name = 'index.html'


class ProductAbout(generic.TemplateView):
    template_name = 'about.html'


class ProductContact(generic.TemplateView):
    template_name = 'contact.html'
