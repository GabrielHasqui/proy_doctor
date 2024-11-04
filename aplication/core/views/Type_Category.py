from django.urls import reverse_lazy
from aplication.core.forms.Type_Category import TypeCategoryForm
from aplication.core.models import TipoCategoria
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class TypeCategoryListView(ListView):
    template_name = "core/type_category/list.html"
    model = TipoCategoria
    context_object_name = 'TiposCategoria'
    query = None
    paginate_by = 5
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')
        if q1 is not None: 
            self.query |= Q(nombre__icontains=q1) 
            self.query |= Q(descripcion__icontains=q1)  
        return self.model.objects.filter(self.query).order_by('nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Tipos de Categoría"
        return context

class TypeCategoryCreateView(CreateView):
    model = TipoCategoria
    template_name = 'core/type_category/form.html'
    form_class = TypeCategoryForm
    success_url = reverse_lazy('core:type_category_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Registro de Tipos de Categoría'
        context['grabar'] = 'Grabar Tipo de Categoría'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        type_category = self.object
        save_audit(self.request, type_category, action='A')
        messages.success(self.request, f"Éxito al crear el tipo de categoría {type_category.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class TypeCategoryUpdateView(UpdateView):
    model = TipoCategoria
    template_name = 'core/type_category/form.html'
    form_class = TypeCategoryForm
    success_url = reverse_lazy('core:type_category_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Actualización de Tipos de Categoría'
        context['grabar'] = 'Actualizar Tipo de Categoría'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        type_category = self.object
        save_audit(self.request, type_category, action='M')
        messages.success(self.request, f"Éxito al actualizar el tipo de categoría {type_category.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class TypeCategoryDeleteView(DeleteView):
    model = TipoCategoria
    template_name = 'core/type_category/delete.html'
    success_url = reverse_lazy('core:type_category_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Eliminar Tipo de Categoría'
        context['grabar'] = f'¿Está seguro de eliminar el tipo de categoría {self.object.nombre}?'
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        type_category = self.get_object()
        save_audit(request, type_category, action='E')
        messages.success(request, f"Éxito al eliminar el tipo de categoría {type_category.nombre}.")
        return super().delete(request, *args, **kwargs)

class TypeCategoryDetailView(DetailView):
    model = TipoCategoria
    
    def get(self, request, *args, **kwargs):
        type_category = self.get_object()
        data = {
            'id': type_category.id,
            'nombre': type_category.nombre,
            'descripcion': type_category.descripcion,
            'valor_minimo': type_category.valor_minimo,
            'valor_maximo': type_category.valor_maximo,
            'activo': type_category.activo,
        }
        return JsonResponse(data)