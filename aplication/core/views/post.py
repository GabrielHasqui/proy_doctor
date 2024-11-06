from django.urls import reverse_lazy
from aplication.core.forms.post import PostForm
from aplication.core.models import Cargo
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class PostListView(ListView):
    model = Cargo
    template_name = 'core/post/list.html'
    context_object_name = 'cargos'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Cargo.objects.filter(
                Q(nombre__icontains=query) |
                Q(descripcion__icontains=query)
            )
        return Cargo.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Consulta de cargos'
        return context
    
class PostCreateView(CreateView):
    model = Cargo
    form_class = PostForm
    template_name = 'core/post/form.html'
    success_url = reverse_lazy('core:post_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        patient = self.object
        save_audit(self.request, patient, action='A')
        messages.success(self.request, f'Éxito al crear el cargo {patient.nombre}.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error al enviar el formulario. Corrige los errores.')
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Crear cargo'
        return context

class PostUpdateView(UpdateView):
    model = Cargo
    form_class = PostForm
    template_name = 'core/post/form.html'
    success_url = reverse_lazy('core:post_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        patient = self.object
        save_audit(self.request, patient, action='M')
        messages.success(self.request, f'Éxito al actualizar el cargo {patient.nombre}.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar el cargo')
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Actualizar cargo'
        return context

class PostDeleteView(DeleteView):
    model = Cargo
    template_name = 'core/post/delete.html'
    success_url = reverse_lazy('core:post_list')
    
    def delete(self, request, *args, **kwargs):
        save_audit(action='delete', model='Cargo', user=self.request.user)
        messages.success(self.request, 'Cargo eliminado con éxito')
        return super().delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Eliminar cargo'
        return context
    
class PostDetailView(DetailView):
    model = Cargo
    
    def get(self, request, *args, **kwargs):
        context = self.get_object()
        data = {
            'id': context.id,
            'nombre': context.nombre,
            'descripcion': context.descripcion,
            'activo': context.activo
        }
        return JsonResponse(data)
