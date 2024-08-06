from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required   #pide staff para el redirect  // hay tambien login y permision
from django.utils.decorators import method_decorator    #Dedocador para el redirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect   #Redirect para usuarios no identificados
from .models import Page
from .forms import PageForm

# class StaffRequiredMixin(object):
#     """
#     Este mixin requerira que el ususario sea miembro del staff
#     """
#     def dispatch(self, request, *args, **kwargs):     #! Se usa para hacer que no se pueda acceder a páginas si no estas logeado como staff
#             if not request.user.is_staff:             # Comprueba si es staff
#                 return redirect(reverse_lazy('admin:login'))
#             return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs) 

class StaffRequiredMixin(object):
    """
    Este mixin requerira que el ususario sea miembro del staff
    """
    @method_decorator(staff_member_required)   #comprueba y luego te redirige a la misma pagina donde estabas
    def dispatch(self, request, *args, **kwargs):     #! Se usa para hacer que no se pueda acceder a páginas si no estas logeado como staff
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs) 


# Create your views here.
class PagesListView(ListView):   #Con las clases te ahorras el escrbir todo el texto de si da error
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy("pages:pages")    

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("pages:update", args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")