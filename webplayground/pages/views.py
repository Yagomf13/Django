from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Page
from .forms import PageForm

# Create your views here.
class PagesListView(ListView):   #Con las clases te ahorras el escrbir todo el texto de si da error
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy("pages:pages")

class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"
    def get_success_url(self):
        return reverse_lazy("pages:update", args=[self.object.id]) + '?ok'

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")