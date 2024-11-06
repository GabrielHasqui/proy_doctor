from django.urls import reverse_lazy
from aplication.core.forms.medicine_brand import Medicine_BrandForm
from aplication.core.models import MarcaMedicamento
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect

class Medicine_BrandListView(ListView):
    model = MarcaMedicamento
    template_name = 'core/medicine_brand/list.html'
    context_object_name = 'medicine_brands'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return MarcaMedicamento.objects.filter(
                Q(nombre__icontains=query) |
                Q(descripcion__icontains=query)
            )
        return MarcaMedicamento.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Consulta de marcas de medicamento'
        return context

class Medicine_BrandCreateView(CreateView):
    model = MarcaMedicamento
    form_class = Medicine_BrandForm
    template_name = 'core/medicine_brand/form.html'
    success_url = reverse_lazy('core:medicine_brand_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        patient = self.object
        save_audit(self.request, patient, action='A')
        messages.success(self.request, f'Éxito al crear la marca de medicamento {patient.nombre}.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error al enviar el formulario. Corrige los errores.')
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Crear marca de medicamento'
        return context

class Medicine_BrandUpdateView(UpdateView):
    model = MarcaMedicamento
    form_class = Medicine_BrandForm
    template_name = 'core/medicine_brand/form.html'
    success_url = reverse_lazy('core:medicine_brand_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        patient = self.object
        save_audit(self.request, patient, action='M')
        messages.success(self.request, f'Éxito al modificar la marca de medicamento {patient.nombre}.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error al enviar el formulario. Corrige los errores.')
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Modificar marca de medicamento'
        return context

class Medicine_BrandDeleteView(DeleteView):
    model = MarcaMedicamento
    template_name = 'core/medicine_brand/delete.html'
    success_url = reverse_lazy('core:medicine_brand_list')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(request, "Marca de Medicamento eliminado con éxito.")
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Esta Marca de medicamento no se puede eliminar porque está en uso en uno o más medicamentos.")
            return redirect(self.success_url)
    
class Medicine_BrandDetailView(DetailView):
    model = MarcaMedicamento

    def get(self, request, *args, **kwargs):
        medicine_brand = self.get_object()
        data = {
            'id': medicine_brand.id,
            'nombre': medicine_brand.nombre,
            'descripcion': medicine_brand.descripcion,
            'activo': medicine_brand.activo,
        }
        return JsonResponse(data)