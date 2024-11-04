from django.urls import reverse_lazy
from aplication.core.forms.Category_Exam import CategoryExamForm
from aplication.core.models import CategoriaExamen
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class CategoryExamListView(ListView):
    template_name = "core/category_exam/list.html"
    model = CategoriaExamen
    context_object_name = 'CategoriasExamen'
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
        context['title1'] = "Consulta de Categorías de Examen"
        return context

class CategoryExamCreateView(CreateView):
    model = CategoriaExamen
    template_name = 'core/category_exam/form.html'
    form_class = CategoryExamForm
    success_url = reverse_lazy('core:category_exam_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Registro de Categorías de Examen'
        context['grabar'] = 'Grabar Categoría de Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        category_exam = self.object
        save_audit(self.request, category_exam, action='A')
        messages.success(self.request, f"Éxito al crear la categoría de examen {category_exam.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class CategoryExamUpdateView(UpdateView):
    model = CategoriaExamen
    template_name = 'core/category_exam/form.html'
    form_class = CategoryExamForm
    success_url = reverse_lazy('core:category_exam_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Actualización de Categorías de Examen'
        context['grabar'] = 'Actualizar Categoría de Examen'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        category_exam = self.object
        save_audit(self.request, category_exam, action='M')
        messages.success(self.request, f"Éxito al actualizar la categoría de examen {category_exam.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class CategoryExamDeleteView(DeleteView):
    model = CategoriaExamen
    template_name = 'core/category_exam/delete.html'
    success_url = reverse_lazy('core:category_exam_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Eliminar Categoría de Examen'
        context['grabar'] = f'¿Está seguro de eliminar la categoría de examen {self.object.nombre}?'
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        category_exam = self.get_object()
        save_audit(request, category_exam, action='E')
        messages.success(request, f"Éxito al eliminar la categoría de examen {category_exam.nombre}.")
        return super().delete(request, *args, **kwargs)

class CategoryExamDetailView(DetailView):
    model = CategoriaExamen
    
    def get(self, request, *args, **kwargs):
        category_exam = self.get_object()
        data = {
            'id': category_exam.id,
            'nombre': category_exam.nombre,
            'descripcion': category_exam.descripcion,
            'activo': category_exam.activo,
        }
        return JsonResponse(data)